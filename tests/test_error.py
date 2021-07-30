import pytest

from compiletojsonschema.compiletojsonschema import CompileToJsonSchema


def test_no_pass():
    """If you do not pass any inputs (eg input_filename, input_schema) it should raise an exception"""
    with pytest.raises(Exception):
        CompileToJsonSchema()
