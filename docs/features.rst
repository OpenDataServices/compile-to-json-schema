Features
========

You can read more on the background at http://os4d.opendataservices.coop/development/schema/#extended-json-schema

Preserve title and description when processing refs
---------------------------------------------------

The standard allows for `$ref` items - however the standard only allows the `$ref` keyword and nothing else.

.. code-block:: json

    {
        "$ref": "#/definitions/address"
    }

Therefore the `title` and `description` are taken from the definition.
However, sometimes we want to provide different values for different uses of the definition.
For example, here we want to describe the home address and the work address differently:

.. code-block:: json

    {
        "definitions": {
            "address": {
                "title": "An Address",
                "description": "A Description",
                "type": "object",
                "properties": {
                    "address": {"type": "string"},
                    "country": {"type": "string"}
                }
            }
        },
        "properties": {
          "home_address": {
            "title": "Home Address",
            "description": "Where the person lives",
            "$ref": "#/definitions/address"
          },
          "work_address": {
            "title": "Work Address",
            "description": "Where the person works",
            "$ref": "#/definitions/address"
          }
        }
    }

This tool will preserve `title` and `description` when resolving refs, producing:

.. code-block:: json

    {
      "properties": {
        "home_address": {
          "properties": {
            "address": {
              "type": "string"
            },
            "country": {
              "type": "string"
            }
          },
          "type": "object",
          "description": "Where the person lives",
          "title": "Home Address"
        },
        "work_address": {
          "properties": {
            "address": {
              "type": "string"
            },
            "country": {
              "type": "string"
            }
          },
          "type": "object",
          "description": "Where the person works",
          "title": "Work Address"
        }
      }
    }


Codelists
---------

If you want to use the enum option, you have to include all the possible options for that JSON in the schema. There may
be some reasons why you don't want to do that:

* The list is very long and makes the schema hard to read or work with.
* The list might be updated from time to time, and you want to make it easy to update (eg a list of currencies).
* You want the options in the list to be used in other places.

You can use the codelist feature - this will take the entries of an enum from an external file.

The external file should be a CSV. The first row will be ignored - so this can be used for headers. The contents of the
first column will be used for enum values. Later columns will be ignored, so you can use them for whatever you want.

So the JSON Schema would look like:

.. code-block:: json

    {
      "properties": {
        "pet": {
          "title": "Pet",
          "codelist": "pets.csv"
        }
      }
    }

And the pets.csv file would look like:

.. code-block:: csv

    Pet,Comment
    Dog,Good
    Cat,Better
    Parrot,Best

And the resulting output would be:

.. code-block:: json

    {
      "properties": {
        "pet": {
          "title": "Pet",
          "codelist": "pets.csv",
          "enum": [
            "Dog",
            "Cat",
            "Parrot"
          ]
        }
      }
    }

You can pass a base directory that will be searched for codelists. If not passed, the current working directory is searched

This will work for situations where one value can be selected and situations with an array where multiple values can be selected.
Set `type:"array"` with the codelist field, and start defining the `"items"` key and the tool will put the enum options on the array items for you.

Finally, if the `openCodelist` variable exists and that is set to true, nothing will be done. This means a codelist is
"Open" (ie - allows the user to add any values they want) as opposed to "Closed" (ie - the user can only add the values
in the codelist).

Set additional properties false everywhere
------------------------------------------

While your schema may welcome additional properties in normal use,
you may want to generate a strict version of your schema that doesn't allow any additional properties.

This can be used for testing - for example, checking your sample data does not have any additional properties.

This is an optional mode, which defaults to off.
