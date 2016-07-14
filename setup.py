from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("Main.py")
)

# build using: python setup.py build_ext --inplace