
cpdef int solution():
    cdef int upper_target = 7*11*13*16*17*18*19*20
    cdef i = 21
    while i < upper_target:
        if i % 1001 == 0:
            print(i)

        for n in range(2,21):
            if i % n != 0:
                break
        else:
            return i

        i += 1

    return -1
