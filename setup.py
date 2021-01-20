import sys

from setuptools import find_packages, setup

extras_require_test = ["pytest", "flake8", "isort"]

if sys.version_info[0] >= 3 and sys.version_info[1] >= 6:
    extras_require_test.append("black==19.10b0")

setup(
    name="compiletojsonschema",
    version="0.2.0",
    author="Open Data Services",
    author_email="code@opendataservices.coop",
    url="https://github.com/OpenDataServices/compile-to-json-schema",
    description="Compile To JSON Schema",
    license="BSD",
    packages=find_packages(),
    long_description="Command-line tools and library for doing some non-standard things with JSON Schema",
    install_requires=["jsonref", "jsonschema",],
    extras_require={"test": extras_require_test,},
    python_requires=">=3.5",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points="""[console_scripts]
compiletojsonschema = compiletojsonschema.cli.__main__:main""",
)
