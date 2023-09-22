import csv
import json
import os
import pathlib
from collections import OrderedDict
from copy import deepcopy

import jsonref


class CompileToJsonSchema:
    def __init__(
        self,
        input_filename=None,
        set_additional_properties_false_everywhere=False,
        codelist_base_directory=None,
        input_schema=None,
    ):
        if not isinstance(input_schema, dict) and not input_filename:
            raise Exception("Must pass input_filename or input_schema")
        self.input_filename = input_filename
        self.input_schema = input_schema
        self.set_additional_properties_false_everywhere = (
            set_additional_properties_false_everywhere
        )
        if codelist_base_directory:
            self.codelist_base_directory = os.path.expanduser(codelist_base_directory)
        else:
            self.codelist_base_directory = os.getcwd()

    def get(self):
        if self.input_filename:
            with open(self.input_filename) as fp:
                resolved = jsonref.load(
                    fp,
                    object_pairs_hook=OrderedDict,
                    base_uri=pathlib.Path(
                        os.path.realpath(self.input_filename)
                    ).as_uri(),
                )
        elif isinstance(self.input_schema, dict):
            resolved = jsonref.JsonRef.replace_refs(self.input_schema)
        else:
            raise Exception("Must pass input_filename or input_schema")

        resolved = self.__process(resolved)

        return resolved

    def get_as_string(self):
        return json.dumps(self.get(), indent=2)

    def __process(self, source):

        out = deepcopy(source)

        if hasattr(source, "__reference__"):
            for attr in list(source.__reference__):
                if not attr == "$ref":
                    out[attr] = source.__reference__[attr]

        if "properties" in source:
            for leaf in list(source["properties"]):
                out["properties"][leaf] = self.__process(source["properties"][leaf])
            if self.set_additional_properties_false_everywhere:
                out["additionalProperties"] = False

        if "items" in source:
            out["items"] = self.__process(source["items"])

        if "oneOf" in source:
            for idx, data in enumerate(list(source["oneOf"])):
                out["oneOf"][idx] = self.__process(source["oneOf"][idx])

        if "anyOf" in source:
            for idx, data in enumerate(list(source["anyOf"])):
                out["anyOf"][idx] = self.__process(source["anyOf"][idx])

        if "allOf" in source:
            for idx, data in enumerate(list(source["allOf"])):
                out["allOf"][idx] = self.__process(source["allOf"][idx])

        if "codelist" in source and (
            "openCodelist" not in source or not source["openCodelist"]
        ):
            filename = os.path.join(self.codelist_base_directory, source["codelist"])
            if os.path.isfile(filename):
                values = []
                with open(filename) as fp:
                    csvreader = csv.reader(fp, delimiter=",", quotechar='"')
                    next(csvreader, None)
                    for row in csvreader:
                        if len(row) > 0 and row[0]:
                            values.append(row[0])
                if values:
                    if out.get("type") == "array" and isinstance(
                        out.get("items"), dict
                    ):
                        out["items"]["enum"] = values
                    else:
                        out["enum"] = values
            else:
                raise CodeListNotFoundException(
                    "Can not find codelist: " + source["codelist"]
                )

        return out


class CodeListNotFoundException(Exception):
    pass
