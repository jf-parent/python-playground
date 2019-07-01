from libc.math cimport sqrt, ceil, log

# Refs:
# https://www.wikiwand.com/en/Baillie%E2%80%93PSW_primality_test
# https://www.wikiwand.com/en/Lucas_pseudoprime#/Strong_Lucas_pseudoprimes
# https://www.wikiwand.com/en/Strong_pseudoprime
# https://www.wikiwand.com/en/Miller%E2%80%93Rabin_primality_test
# https://github.com/smllmn/baillie-psw
# https://www.wikiwand.com/en/Prime_number_theorem
# https://codereview.stackexchange.com/questions/188053/project-euler-problem-7-in-python-10001st-prime-number

cdef miller_rabin_base_2(int n):
    cdef int d = n - 1
    cdef int s = 0
    cdef int x

    while not d & 1:
        d = d >> 1
        s += 1

    x = pow(2, d, n)
    if x == 1 or x == n-1:
        return True

    for i in range(s-1):
        x = pow(x, 2, n)
        if x == 1:
            return False
        elif x == n - 1:
            return True

    return False

cdef get_U_V(int k, int n, int U, int V, int P, int Q, int D):
    digits = list(map(int, str(bin(k))[2:]))
    cdef int i = 1
    for digit in digits[1:]:
        U, V = U*V % n, (pow(V, 2, n) - 2*pow(Q, i, n)) % n
        i *= 2
        if digit == 1:
            if not (P*U + V) & 1:
                if not (D*U + P*V) & 1:
                    U, V = (P*U + V) >> 1, (D*U + P*V) >> 1
                else:
                    U, V = (P*U + V) >> 1, (D*U + P*V + n) >> 1
            elif not (D*U + P*V) & 1:
                U, V = (P*U + V + n) >> 1, (D*U + P*V) >> 1
            else:
                U, V = (P*U + V + n) >> 1, (D*U + P*V + n) >> 1
            i += 1
            U, V = U % n, V % n
    return [U, V]

cdef lucas_pp(int n, int D, int P, int Q):
    U_V = get_U_V(n+1, n, 1, P, P, Q, D)
    cdef int U = U_V[0]
    cdef int V = U_V[1]

    if U != 0:
        return False

    cdef int d = n + 1
    cdef int s = 0
    while not d & 1:
        d = d >> 1
        s += 1

    U_V = get_U_V(n+1, n, 1, P, P, Q, D)
    U = U_V[0]
    V = U_V[1]

    if U == 0:
        return True

    for r in range(s):
        U = (U*V) % n
        V = (pow(V, 2, n) - 2*pow(Q, d*(2**r), n)) % n
        if V == 0:
            return True

    return False

cdef int jacobi_symbol(int a, int n):
    if n == 1:
        return 1
    elif a == 0:
        return 0
    elif a == 1:
        return 1
    elif a == 2:
        if n % 8 in [3, 5]:
            return -1
        elif n % 8 in [1, 7]:
            return 1
    elif a < 0:
        return (-1)**((n-1)/2) * jacobi_symbol(-1*a, n)

    if a % 2 == 0:
        return jacobi_symbol(2, n) * jacobi_symbol(a / 2, n)
    elif a % n != a:
        return jacobi_symbol(a % n, n)
    else:
        if a % 4 == n % 4 == 3:
            return -1 * jacobi_symbol(n, a)
        else:
            return jacobi_symbol(n, a)

cdef int find_D(int candidate):
    cdef int D = 5
    while jacobi_symbol(D, candidate) != -1:
        D += 2 if D > 0 else -2
        D *= -1
    return D

cdef baillie_psw(int candidate):
    if not miller_rabin_base_2(candidate):
        return False

    if sqrt(candidate).is_integer():
        return False

    cdef int D = find_D(candidate)
    cdef int DD = int((1-D)/4)
    if not lucas_pp(candidate, D, 1, DD):
        return False

    return True

cdef upper_bound_for_p_n(int n):
    if n < 6:
        return 100
    return ceil(n * (log(n) + log(log(n))))

def find_primes(int limit):
    nums = [True] * (limit + 1)
    nums[0] = nums[1] = False

    for (i, is_prime) in enumerate(nums):
        if is_prime:
            yield i
            for n in range(i * i, limit + 1, i):
                nums[n] = False

def solution(n):
    primes = list(find_primes(upper_bound_for_p_n(n)))
    return primes[n - 1]
