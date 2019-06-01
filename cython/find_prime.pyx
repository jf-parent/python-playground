

cpdef int find_prime_greater_than(int n):
    cdef int i = n + 1
    cdef int a
    while True:
        for a in range(2, i):
            if i % a == 0:
                break
        else:
            return i
        i += 1
