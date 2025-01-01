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
        # These vars hold output
        self._processed = False
        self._output_json = None
        self._output_types_used = None
        self._output_keywords_used = None

    def get(self):
        self.__process()
        return self._output_json

    def get_as_string(self):
        return json.dumps(self.get(), indent=2)

    def get_types_used(self):
        self.__process()
        return sorted(self._output_types_used.keys())

    def get_keywords_used(self):
        self.__process()
        return sorted(self._output_keywords_used.keys())

    def __process(self):
        # If already processed, return .....
        if self._processed:
            return

        # Process now ....
        self._output_types_used = {}
        self._output_keywords_used = {}
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
        self._output_json = self.__process_data(resolved)
        self._processed = True

    def __process_data(self, source):

        out = deepcopy(source)

        for keyword in source:
            self._output_keywords_used[keyword] = {}

        if "type" in source:
            if isinstance(source["type"], str):
                self._output_types_used[source["type"]] = {}
            elif isinstance(source["type"], list):
                for t in source["type"]:
                    if isinstance(t, str):
                        self._output_types_used[t] = {}

        if hasattr(source, "__reference__"):
            self._output_keywords_used["$ref"] = {}
            for attr in list(source.__reference__):
                if not attr == "$ref":
                    out[attr] = source.__reference__[attr]

        if "properties" in source:
            for leaf in list(source["properties"]):
                out["properties"][leaf] = self.__process_data(
                    source["properties"][leaf]
                )
            if self.set_additional_properties_false_everywhere:
                out["additionalProperties"] = False

        if "items" in source:
            out["items"] = self.__process_data(source["items"])

        if "oneOf" in source:
            for idx, data in enumerate(list(source["oneOf"])):
                out["oneOf"][idx] = self.__process_data(source["oneOf"][idx])

        if "anyOf" in source:
            for idx, data in enumerate(list(source["anyOf"])):
                out["anyOf"][idx] = self.__process_data(source["anyOf"][idx])

        if "allOf" in source:
            for idx, data in enumerate(list(source["allOf"])):
                out["allOf"][idx] = self.__process_data(source["allOf"][idx])

        if "dependentSchemas" in source and isinstance(
            source["dependentSchemas"], dict
        ):
            for k, v in source["dependentSchemas"].items():
                out["dependentSchemas"][k] = self.__process_data(v)

        for keyword in ["if", "then", "else"]:
            if keyword in source:
                out[keyword] = self.__process_data(source[keyword])

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
