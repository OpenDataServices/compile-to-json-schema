from setuptools import setup, find_packages

setup(
    name='complietojsonschema',
    version='0.0.0',
    author='Open Data Services',
    author_email='code@opendataservices.coop',
    url='https://github.com/OpenDataServices/compile-to-json-schema',
    description='Compile To JSON Schema',
    license='BSD',
    packages=find_packages(),
    long_description='A suite of command-line tools for working with BODS data',
    install_requires=[
        'jsonref',
        'jsonschema',
    ],
    extras_require={
        'test': [
            'pytest',
            'flake8',
        ],
    },
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points='''[console_scripts]
compiletojsonschema = compiletojsonschema.cli.__main__:main''',
)
