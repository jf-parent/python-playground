
cpdef solution():
    cdef int sum_of_squares_100 = 0
    cdef int square_of_sum_100 = 0
    cdef int i
    for i in range(1, 101):
        sum_of_squares_100 += i*i
        square_of_sum_100 += i
    square_of_sum_100 *= square_of_sum_100

    return square_of_sum_100 - sum_of_squares_100 
