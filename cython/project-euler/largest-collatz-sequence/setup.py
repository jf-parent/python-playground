from distutils.core import setup
from Cython.Build import cythonize

setup(name='Project Euler Solution',
      ext_modules=cythonize("*.pyx"))
