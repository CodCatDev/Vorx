import os
import sys
sys.argv = ["build.py", "build_ext", "--inplace", "-q"]
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

print("Compiling Cython modules...")
setup(
    ext_modules=cythonize(extensions, quiet=True)
)

print("Build complete. Cleaning up cache files...")

for mod in modules:
    c_file = f"{mod}.c"
    if os.path.exists(c_file):
        os.remove(c_file)
        print(f"cache deleted: {c_file}")

print("All done!")
