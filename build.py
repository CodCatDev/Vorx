import os
import sys
from setuptools import setup, Extension
from Cython.Build import cythonize

print("VorxEngine build script")

modules = [
    "vorx/core/maths/vectors"
]

extensions = []
for mod in modules:
    module_name = mod.replace("/", ".")
    source_file = f"{mod}.pyx"
    
    extensions.append(Extension(name=module_name, sources=[source_file]))

sys.argv = ["build.py", "build_ext", "--inplace"]

print("Compiling Cython modules...")
setup(
    ext_modules=cythonize(extensions)
)

print("Build complete. Cleaning up cache files...")

for mod in modules:
    c_file = f"{mod}.c"
    if os.path.exists(c_file):
        os.remove(c_file)
        print(f"cache deleted: {c_file}")

print("All done!")
