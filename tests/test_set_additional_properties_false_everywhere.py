import json
import os

from compiletojsonschema.compiletojsonschema import CompileToJsonSchema


def test_basic():

    input_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "set-additional-properties-false-everywhere",
        "test_basic.json",
    )

    ctjs = CompileToJsonSchema(
        input_filename=input_filename, set_additional_properties_false_everywhere=True
    )
    out_string = ctjs.get_as_string()
    out = json.loads(out_string)

    assert type(out["additionalProperties"]) == bool
    assert not out["additionalProperties"]

    assert type(out["properties"]["home_address"]["additionalProperties"]) == bool
    assert not out["properties"]["home_address"]["additionalProperties"]

    assert type(out["properties"]["work_address"]["additionalProperties"]) == bool
    assert not out["properties"]["work_address"]["additionalProperties"]


def test_already_set():

    input_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "set-additional-properties-false-everywhere",
        "test_already_set.json",
    )

    ctjs = CompileToJsonSchema(
        input_filename=input_filename, set_additional_properties_false_everywhere=True
    )
    out_string = ctjs.get_as_string()
    out = json.loads(out_string)

    assert type(out["additionalProperties"]) == bool
    assert not out["additionalProperties"]

    assert type(out["properties"]["home_address"]["additionalProperties"]) == bool
    assert not out["properties"]["home_address"]["additionalProperties"]

    assert type(out["properties"]["work_address"]["additionalProperties"]) == bool
    assert not out["properties"]["work_address"]["additionalProperties"]
