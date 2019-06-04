from libc.math cimport sin

cpdef double sinf(double x):
    return sin(x * x)
