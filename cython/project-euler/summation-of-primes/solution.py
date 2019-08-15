def solution(upper_bound):
    is_primes = [True] * (upper_bound + 1)
    is_primes[0] = is_primes[1] = False
    sum_of_primes = 0

    for i, is_prime in enumerate(is_primes):
        if is_prime:
            sum_of_primes += i
            print("i", i)
            print("sum_of_primes", sum_of_primes)
            for n in range(i*i, upper_bound + 1 , i):
                is_primes[n] = False

    return sum_of_primes
