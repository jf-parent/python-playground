
cpdef int solution(int limit):
    cdef int last_fib = 1
    cdef int cur_fib = 2
    cdef int answer = 0
    while cur_fib < limit:
        if cur_fib % 2 == 0:
            answer += cur_fib

        next_fib = cur_fib + last_fib
        last_fib = cur_fib
        cur_fib = next_fib

    return answer
