from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
    Extension("solution",
              sources=["solution.pyx"],
              libraries=["m"]
              )
]

setup(name='Project Euler Solution',
      ext_modules=cythonize(ext_modules))
