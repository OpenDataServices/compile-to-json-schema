import argparse
from compiletojsonschema.compiletojsonschema import CompileToJsonSchema


def main():
    parser = argparse.ArgumentParser(description='Compile To JSON Schema CLI')

    parser.add_argument('input_file')

    args = parser.parse_args()

    ctjs = CompileToJsonSchema(input_filename=args.input_file)
    print(ctjs.get_as_string())
