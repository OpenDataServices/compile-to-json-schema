import json
import os

import jsonref
import pytest

from compiletojsonschema.compiletojsonschema import CompileToJsonSchema


def test_urn():

    input_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "urn",
        "schema.json",
    )

    lib_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "urn",
        "library.json",
    )

    ctjs = CompileToJsonSchema(
        input_filename=input_filename, load_urn_schema_filenames=[lib_filename]
    )
    out_string = ctjs.get_as_string()
    out = json.loads(out_string)

    assert out["properties"]["work_address"]["title"] == "Work Address"
    assert out["properties"]["work_address"]["description"] == "Where the person works"
    assert (
        out["properties"]["work_address"]["properties"]["address"]["type"] == "string"
    )
    assert out["properties"]["home_address"]["title"] == "Home Address"
    assert out["properties"]["home_address"]["description"] == "Where the person lives"
    assert (
        out["properties"]["home_address"]["properties"]["address"]["type"] == "string"
    )


def test_urn_not_loaded():

    input_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "urn",
        "schema.json",
    )

    ctjs = CompileToJsonSchema(input_filename=input_filename)

    with pytest.raises(jsonref.JsonRefError):
        ctjs.get_as_string()
