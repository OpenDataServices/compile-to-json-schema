Installing
==========

To install,

1) Check out the git repository ( https://github.com/OpenDataServices/compile-to-json-schema ) onto your machine.

2) In that directory, create a new Python Virtual Environment (or similar, using the tool of your choice).

3) To install the tool and it's dependencies, run:

.. code-block:: shell-session

    pip install -e .

If you will want to develop the tool, instead run:

.. code-block:: shell-session

    pip install -e .[test]

4) The tool should now be available! Run


.. code-block:: shell-session

    compiletojsonschema --help
