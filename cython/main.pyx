
cpdef float some_math(int a, int b, double c):
    cdef int i
    cdef double answer
    for i in range(a+100):
        answer = (((b + i) ** c) / 3) * 2.0
    return answer

cpdef double f(double x) except? -2:
    return x ** 2 - x
