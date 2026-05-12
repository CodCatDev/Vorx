# All Change Log history

## [2026.0.2-dev] - 2026-05-12

A "Core" update

### Added
- New CLI command - `init`
- Started working on the main core of the engine
- Added dependencies and setup instructions for the engine to ReadMe
- Added `Vector2` class, with functions `length`, `normalized`, `normalize` (vorx/core/maths/vectors.pyx)
- Added `build.py` script for building the engine Cython (.pyx) components to C. For more speed and better performance.

### Fixed
- Fixed a bug in the CLI with ping (On Server-Side)

<hr>

## [2026.0.1.1-dev] - 2026-05-09

A mini patch update

### Added
- New version numbering - calver (calendar versioning) (Year.Major.Minor)
- Rewrite a CLI client for a more scalable structure
- New CLI command - `version`

### Fixed
- Fix a ping bug in the CLI

<hr>

## [26.0.1-dev] - 2026-05-08

First dev version! Starting development

### Added
- Windows x64 SDL2 libs
- Base engine structure
- CLI client