import timeit

print("List prime")
cython_t = timeit.timeit("primescy(1000)", setup="from list_prime import primescy", number=10)
print('cython_t', cython_t)

cythoncpp_t = timeit.timeit("primescpp(1000)", setup="from list_primecpp import primescpp", number=10)
print('cythoncpp_t', cythoncpp_t)

python_t = timeit.timeit("primespy(1000)", setup="from list_prime_py import primespy", number=10)
print('python_t', python_t)

exit()

print("Find prime")
cython_t = timeit.timeit("find_prime.find_prime_greater_than(1000000)", setup="import find_prime", number=1)
print(cython_t)

python_t = timeit.timeit("find_prime_py.find_prime_greater_than(1000000)", setup="import find_prime_py", number=1)
print(python_t)

print((python_t/cython_t)*100)

print("Some Math")
cython_t = timeit.timeit("main.some_math(10, 5, 10.0)", setup="import main", number=1000)

python_t = timeit.timeit("main_py.some_math(10, 5, 10.0)", setup="import main_py", number=1000)

print((python_t/cython_t)*100)

print("f")
cython_t = timeit.timeit("main.f(100000)", setup="import main", number=1000)

python_t = timeit.timeit("main_py.f(100000)", setup="import main_py", number=1000)

print((python_t/cython_t)*100)

