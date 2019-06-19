import cython
from libc.math cimport sqrt, floor

cdef bint is_prime(long n):

    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return 0

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return 0
        i += 6

    return 1

@cython.cdivision(True)
cpdef long solution(long target):
    cdef long number = target / 2
    while number > 2:
        if target % number == 0:
            if is_prime(number):
                return number
        number -= 2
        if number % 1001 == 0:
            print(number)
    return -1
