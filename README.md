<div align="center">
    <img src="assets/logo.png" alt="Vorx Engine Logo" width="200">
    <h1>Vorx Engine</h1>
    <h2>2026.0.5.1-DEV</h2>
    <p>
        <a href="CHANGELOG.md">
            <img src="https://img.shields.io/badge/Build-2026.0.5--DEV-blue?style=flat" alt="Build">
        </a>
        <img src="https://img.shields.io/badge/Python-3.8%2B-yellow?style=flat&logo=python" alt="Python">
        <img src="https://img.shields.io/badge/License-Apache%202.0-blue?style=flat" alt="License">
    </p>
</div>

# Structure

- [Structure](#structure)
- [Overview](#overview)
- [Builds](#builds)
- [Installations](#installations)
    - [Releases](#installations-via-releases)
    - [Git](#installations-via-git)
        - [Stable](#stable-builds)
        - [Dev](#dev-builds)
    - [Setup](#setup)
        - [Windows](#windows)
        - [Linux](#linux)
        - [Mac](#mac)

# Overview

Vorx is an engine for creating 2D games, written on Python. It is built on top of the [SDL2](https://www.libsdl.org/) library.

# Builds

Currently there are no releases. All code for Dev builds is available [here](https://github.com/CodCatDev/Vorx/tree/dev)

# Installations

## Installations via Releases
If you are installing Vorx, get a stable build from [Latest Release](https://github.com/CodCatDev/Vorx/releases/latest) on github, if there are no releases, install directly from Git

For install you need dependencies:

- [Python 3.8+](https://www.python.org/)
- [Pip](https://pypi.org/project/pip/)
- [setuptools](https://setuptools.pypa.io/en/latest/)

## Installations via Git

If you installing Vorx from Git, you need a dependencies to build it from source:

- [Python 3.8+](https://www.python.org/)
- [Cython](https://cython.org/) and [setuptools](https://setuptools.pypa.io/en/latest/)
- [Pip](https://pypi.org/project/pip/)
- C Compiler:
  - Windows: [Microsoft Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
  - Linux: [build-essential (gcc)](https://packages.ubuntu.com/focal/build-essential)
  - Mac: [Xcode Command Line Tools](https://developer.apple.com/download/more/)

### Stable builds
For install stable builds from git, use the following command
```bash
git clone https://github.com/CodCatDev/Vorx.git
```

### Dev builds

For install dev builds from git, use the following command
```bash
git clone --branch dev https://github.com/CodCatDev/Vorx.git
```

## Setup

### Windows

If you install from `git`, run this commands to build engine core:

```bash
cd Vorx
pip install -r requirements.txt
python build.py
```

If you install from `releases`, all be done!

### Linux

Install a Sdl2 Libs
```bash
sudo apt-get update
sudo apt-get install libsdl2-2.0-0 libsdl2-dev
```

For arch:
```bash
sudo pacman -S sdl2
```

For Fedora/RHEL:
```bash
sudo dnf install SDL2-devel
```

And build engine core, with libs:
```bash
cd Vorx
pip3 install -r requirements.txt
python3 build.py
```

### Mac

Install [Homebrew](https://brew.sh/)

download SDL2-dev
```bash
brew install sdl2
```

install all and build
```bash
cd Vorx
pip3 install -r requirements.txt
python3 build.py
```