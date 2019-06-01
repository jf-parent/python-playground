from distutils.core import setup
from Cython.Build import cythonize

setup(name='Cython Playground',
      ext_modules=cythonize("*.pyx", annotate=True))
