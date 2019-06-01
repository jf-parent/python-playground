
def find_prime_greater_than(n):
    i = n + 1
    while True:
        for a in range(2, i):
            if i % a == 0:
                break
        else:
            return i
        i += 1
