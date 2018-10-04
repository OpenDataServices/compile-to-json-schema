import jsonref
import json
import pathlib
import os
from copy import deepcopy


class CompileToJsonSchema:

    def __init__(self, input_filename):
        self.input_filename = input_filename

    def get(self):
        with open(self.input_filename) as fp:
            resolved = jsonref.load(fp, base_uri=pathlib.Path(os.path.realpath(self.input_filename)).as_uri())

        resolved = self.__process(resolved)

        return resolved

    def get_as_string(self):
        return json.dumps(self.get(), indent=2)

    def __process(self, source):

        out = deepcopy(source)

        if hasattr(source, '__reference__'):
            for attr in list(source.__reference__):
                if not attr == "$ref":
                    out[attr] = source.__reference__[attr]

        if 'properties' in source:
            for leaf in list(source['properties']):
                out['properties'][leaf] = self.__process(source['properties'][leaf])

        if 'items' in source:
            out['items'] = self.__process(source['items'])

        if 'oneOf' in source:
            for idx, data in enumerate(list(source['oneOf'])):
                out['oneOf'][idx] = self.__process(source['oneOf'][idx])

        return out
