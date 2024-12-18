import argparse

from compiletojsonschema.compiletojsonschema import CompileToJsonSchema


def main():
    parser = argparse.ArgumentParser(description="Compile To JSON Schema CLI")

    parser.add_argument("input_file")
    parser.add_argument(
        "-s",
        "--set-additional-properties-false-everywhere",
        action="store_true",
        help="Set Additional Properties False everywhere? This generates strict schemas that can be used for testing.",
    )
    parser.add_argument(
        "-c",
        "--codelist-base-directory",
        help="Which directory we should look in for codelists",
    )
    parser.add_argument(
        "-u",
        "--urn-schema-filename",
        help="Filenames of additional schemas to load and refer to by URN later while processing the input file",
        action="append",
    )

    args = parser.parse_args()

    ctjs = CompileToJsonSchema(
        input_filename=args.input_file,
        set_additional_properties_false_everywhere=args.set_additional_properties_false_everywhere,
        codelist_base_directory=args.codelist_base_directory,
        load_urn_schema_filenames=args.urn_schema_filename or [],
    )
    print(ctjs.get_as_string())
