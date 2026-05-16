# All Change Log history

## [2026.0.5-dev] - 2026-05-16

Rework MAANY things! :D

### Added
- Switched to raw C pointers and batched geometry rendering.
- Zero Python overhead in the render loop -> insane FPS increase.
- Demo of the scene parser
- GithubActions
- New Windows Libs
- New Install instructions
- Demo scene in `test/`

## [2026.0.4-dev] - 2026-05-15

Yeaa! new vectors and windows!

### Added
- Added In-place operations (+= -= *= /=) to `Vector2`
- Added internal `asVec2()` method, returning a `Vec2` struct for C-level conversions
- Added `.gitattributes` file for github language detection
- Added a `shapes.pyx` with `Rect`, `Polygon` and `Shape` classes
- Added a `Renderer`, written in Cython
- Added a DocString to `Vector2`, `Shapes` and `Renderer`
- Added a demo scene (`demo.py`)

## [2026.0.3.1-dev] - 2026-05-14

Many fixes and rework

### Added
- Rework the CLI cmd names system
- Added the `dot`, `distanceTo`, `length` and his squared versions to the `Vector2` class (vorx/core/maths/vectors.pyx)
- Added a `SDL2` libs for `MacOS`, `arm64` and `x64` (lib/macosx)
- Added a `SDL2` libs for `Linux`, `x64` (lib/linux)

### Fixes
- Fixed a bug involving the redefinition of standard functions (`help`, `list`) (vorx/cli/commands/main.py)

## [2026.0.3-dev] - 2026-05-13

Fixes and updates

### Added
- Print a server status in the `ping` command
- Replaced `socket tcp` with `http head` in `ping` command
- Added colors to the CLI
- Started working on the main render/window of the engine
- Added OS detect to the core, for libs loading

### Fixed
- Fixed a bug with status in `ping` command
- Fixed a `FileExistsError` in `init` command 

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