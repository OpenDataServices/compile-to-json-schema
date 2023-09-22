# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Process anyOf and allOf and well as oneOf https://github.com/OpenDataServices/compile-to-json-schema/issues/28
- When codelist is used on an array, the enum is set for items in that array

### Removed

- Removed Python 3.5 and 3.6 support, as they aren't supported any more

## [0.4.0] - 2021-07-30

### Added

- Can pass schema to Python class as well as filename

## [0.3.0] - 2021-01-27

### Added

- Codelist feature https://github.com/OpenDataServices/compile-to-json-schema/issues/2

### Changes

- Specify a minimum Python version, and set that to be 3.5

## [0.2.0] - 2020-07-07                                                 

### Fixed

- Corrected Spelling of package name in setup.py


## [0.1.0] - 2019-08-04

### Added

- Preserve title and description when processing refs feature
- Set additional properties false everywhere option https://github.com/OpenDataServices/compile-to-json-schema/issues/3

