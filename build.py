from setuptools import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import sys

inc_dirs = []
lib_dirs = []
libs = ["SDL2"]
compile_args = []

if sys.platform == "win32":
    inc_dirs = ["lib/win/cInc"]
    lib_dirs = ["lib/win/cLibs"]
    compile_args = ["/O2"]
elif sys.platform.startswith("linux"):
    inc_dirs = ["/usr/include/SDL2"]
    compile_args = ["-O3"]
elif sys.platform == "darwin":
    inc_dirs = ["/opt/homebrew/include/SDL2", "/usr/local/include/SDL2"]
    lib_dirs = ["/opt/homebrew/lib", "/usr/local/lib"]
    compile_args = ["-O3"]

ext = [
    Extension(
        "vorx.objects.shapes",
        ["vorx/objects/shapes.pyx"],
        extra_compile_args=compile_args
    ),
    Extension(
        "vorx.core.maths.vectors",
        ["vorx/core/maths/vectors.pyx"],
        extra_compile_args=compile_args
    ),
    Extension(
        "vorx.core.renderer",
        ["vorx/core/renderer.pyx"],
        include_dirs=inc_dirs,
        library_dirs=lib_dirs,
        libraries=libs,
        extra_compile_args=compile_args
    )
]

setup(
    ext_modules=cythonize(ext),
    script_args=['build_ext', '--inplace']
)
