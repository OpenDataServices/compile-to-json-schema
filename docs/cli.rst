Command line tool
=================


You can use the tool with the provided CLI script.

Pass a filename of an input schema.

.. code-block:: shell-session

    compiletojsonschema input.json

The output is printed. To save the output to file, simple redirect it:

.. code-block:: shell-session

    compiletojsonschema input.json > output.json

Set a directory for codelists
-----------------------------

You can set the directory that is searched for codelists using the `--codelist-base-directory` or `-c` flag.

.. code-block:: shell-session

    compiletojsonschema -c data/codelists schema.json
    compiletojsonschema --codelist-base-directory data/codelists schema.json


Set additional properties false everywhere
------------------------------------------

To enable this mode, pass the `--set-additional-properties-false-everywhere` or `-s` flag.


.. code-block:: shell-session

    compiletojsonschema -s input.json
    compiletojsonschema --set-additional-properties-false-everywhere input.json

Get Audit output
----------------

Instead of the compiled JSON schema, you can get an audit output by passing the `--audit` or `-a` flag.


.. code-block:: shell-session

    compiletojsonschema -a input.json
    compiletojsonschema --audit input.json
