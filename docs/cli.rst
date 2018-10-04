Command line tool
=================


You can use the tool with the provided CLI script.

Pass a filename of an input schema.

.. code-block:: shell-session

    compiletojsonschema input.json

The output is printed. To save the output to file, simple redirect it:

.. code-block:: shell-session

    compiletojsonschema input.json > output.json


Set additional properties false everywhere
------------------------------------------

To enable this mode, pass the `--set-additional-properties-false-everywhere` flag.


.. code-block:: shell-session

    compiletojsonschema --set-additional-properties-false-everywhere input.json
