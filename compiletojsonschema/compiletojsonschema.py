import json
import os
import pathlib
from collections import OrderedDict
from copy import deepcopy

import jsonref


class CompileToJsonSchema:
    def __init__(
        self, input_filename, set_additional_properties_false_everywhere=False
    ):
        self.input_filename = input_filename
        self.set_additional_properties_false_everywhere = (
            set_additional_properties_false_everywhere
        )

    def get(self):
        with open(self.input_filename) as fp:
            resolved = jsonref.load(
                fp,
                object_pairs_hook=OrderedDict,
                base_uri=pathlib.Path(os.path.realpath(self.input_filename)).as_uri(),
            )

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

        return out
