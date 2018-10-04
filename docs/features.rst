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
