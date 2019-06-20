
cpdef find_largest_palindrome_product_3digits():
    cdef int i, j, p, answer
    answer = 0
    for i in range(100,1000):
        for j in range(i+1, 1000):
            p = i * j
            if p < 100000: continue

            if i % 100:
                print(i,j,p)
            firstn = p % 1000000 / 100000
            secondn = p % 100000 / 10000
            thirdn = p % 10000 / 1000
            fourthn = p % 1000 / 100
            fifthn = p % 100 / 10
            sixthn = p % 10
            if firstn == sixthn and secondn == fifthn and thirdn == fourthn:
                answer = max(answer,p)
    return answer
