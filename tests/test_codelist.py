import os

import pytest

from compiletojsonschema.compiletojsonschema import (
    CodeListNotFoundException,
    CompileToJsonSchema,
)

# The pets.csv file has many new lines at the end deliberately so we can test it won't try and load them.


def test_not_found():

    input_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "codelists",
        "schema.json",
    )

    # This is deliberately the wrong value so that an exception should be thrown
    codelist_dir = os.path.dirname(os.path.realpath(__file__))

    with pytest.raises(CodeListNotFoundException):
        CompileToJsonSchema(
            input_filename=input_filename, codelist_base_directory=codelist_dir
        ).get()


def test_basic():

    # schema.json has no openCodelist value deliberately so we can test the default options.
    input_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "codelists",
        "schema.json",
    )

    codelist_dir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "codelists",
    )

    ctjs = CompileToJsonSchema(
        input_filename=input_filename, codelist_base_directory=codelist_dir
    )
    out = ctjs.get()

    assert out["properties"]["pet"]["enum"] == ["Dog", "Cat", "Parrot"]


def test_open_codelist():

    input_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "codelists",
        "schema-open-codelist.json",
    )

    codelist_dir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "codelists",
    )

    ctjs = CompileToJsonSchema(
        input_filename=input_filename, codelist_base_directory=codelist_dir
    )
    out = ctjs.get()

    assert "enum" not in out["properties"]["pet"]


def test_closed_codelist():

    input_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "codelists",
        "schema-closed-codelist.json",
    )

    codelist_dir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "codelists",
    )

    ctjs = CompileToJsonSchema(
        input_filename=input_filename, codelist_base_directory=codelist_dir
    )
    out = ctjs.get()

    assert out["properties"]["pet"]["enum"] == ["Dog", "Cat", "Parrot"]


def test_closed_codelist_array():

    input_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "codelists",
        "schema-closed-codelist-array.json",
    )

    codelist_dir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "codelists",
    )

    ctjs = CompileToJsonSchema(
        input_filename=input_filename, codelist_base_directory=codelist_dir
    )
    out = ctjs.get()

    assert not out["properties"]["pet"].get("enum")
    assert out["properties"]["pet"]["items"]["enum"] == ["Dog", "Cat", "Parrot"]
