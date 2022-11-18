import json
import os
from collections import OrderedDict

from compiletojsonschema.compiletojsonschema import CompileToJsonSchema


def test_in_file():

    input_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "simple",
        "in_file.json",
    )

    ctjs = CompileToJsonSchema(input_filename=input_filename)
    out_string = ctjs.get_as_string()
    out = json.loads(out_string)

    assert out["properties"]["work_address"]["title"] == "Work Address"
    assert out["properties"]["work_address"]["description"] == "Where the person works"
    assert out["properties"]["home_address"]["title"] == "Home Address"
    assert out["properties"]["home_address"]["description"] == "Where the person lives"


def test_in_file_pass_as_schema():

    input_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "simple",
        "in_file.json",
    )

    with open(input_filename) as fp:
        input_schema = json.load(
            fp,
            object_pairs_hook=OrderedDict,
        )

    ctjs = CompileToJsonSchema(input_schema=input_schema)
    out_string = ctjs.get_as_string()
    out = json.loads(out_string)

    assert out["properties"]["work_address"]["title"] == "Work Address"
    assert out["properties"]["work_address"]["description"] == "Where the person works"
    assert out["properties"]["home_address"]["title"] == "Home Address"
    assert out["properties"]["home_address"]["description"] == "Where the person lives"


def test_file_main():

    input_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "simple",
        "file-main.json",
    )

    ctjs = CompileToJsonSchema(input_filename=input_filename)
    out_string = ctjs.get_as_string()
    out = json.loads(out_string)

    assert out["properties"]["work_address"]["title"] == "Work Address"
    assert out["properties"]["work_address"]["description"] == "Where the person works"
    assert out["properties"]["home_address"]["title"] == "Home Address"
    assert out["properties"]["home_address"]["description"] == "Where the person lives"


def test_file_list_anyof():

    input_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "simple",
        "file-list-anyof.json",
    )

    ctjs = CompileToJsonSchema(input_filename=input_filename)
    out_string = ctjs.get_as_string()
    out = json.loads(out_string)

    assert out["items"]["anyOf"][0]["properties"]["address"]["title"] == "Home Address"
    assert (
        out["items"]["anyOf"][0]["properties"]["address"]["description"]
        == "Where the person lives"
    )
    assert out["items"]["anyOf"][1]["properties"]["address"]["title"] == "Work Address"
    assert (
        out["items"]["anyOf"][1]["properties"]["address"]["description"]
        == "Where the person works"
    )


def test_file_list_oneof():

    input_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "simple",
        "file-list-oneof.json",
    )

    ctjs = CompileToJsonSchema(input_filename=input_filename)
    out_string = ctjs.get_as_string()
    out = json.loads(out_string)

    assert out["items"]["oneOf"][0]["properties"]["address"]["title"] == "Home Address"
    assert (
        out["items"]["oneOf"][0]["properties"]["address"]["description"]
        == "Where the person lives"
    )
    assert out["items"]["oneOf"][1]["properties"]["address"]["title"] == "Work Address"
    assert (
        out["items"]["oneOf"][1]["properties"]["address"]["description"]
        == "Where the person works"
    )


def test_file_list_allof():

    input_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "simple",
        "file-list-allof.json",
    )

    ctjs = CompileToJsonSchema(input_filename=input_filename)
    out_string = ctjs.get_as_string()
    out = json.loads(out_string)

    assert out["items"]["allOf"][0]["properties"]["address"]["title"] == "Home Address"
    assert (
        out["items"]["allOf"][0]["properties"]["address"]["description"]
        == "Where the person lives"
    )


def test_passing_empty_schema_is_ok():
    ctjs = CompileToJsonSchema(input_schema={})
    assert "{}" == ctjs.get_as_string()
