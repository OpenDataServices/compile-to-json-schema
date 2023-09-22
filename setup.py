from setuptools import find_packages, setup

extras_require_test = ["pytest", "flake8", "isort", "black==22.10.0"]

setup(
    name="compiletojsonschema",
    version="0.5.0",
    author="Open Data Services",
    author_email="code@opendataservices.coop",
    url="https://github.com/OpenDataServices/compile-to-json-schema",
    description="Compile To JSON Schema",
    license="BSD",
    packages=find_packages(),
    long_description="Command-line tools and library for doing some non-standard things with JSON Schema",
    install_requires=[
        "jsonref",
        "jsonschema",
    ],
    extras_require={
        "test": extras_require_test,
    },
    python_requires=">=3.7",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    entry_points="""[console_scripts]
compiletojsonschema = compiletojsonschema.cli.__main__:main""",
)
