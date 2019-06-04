
cpdef int solution(int n):
    cdef int answer = 0
    cdef int index

    for index in range(3, n):
        if index % 3 == 0 or index % 5 == 0:
            answer += index

    return answer
