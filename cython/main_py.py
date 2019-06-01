
def some_math(a, b, c):
    for i in range(a):
        answer = (b + i) * c
    return answer

def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b

def f(x):
    return x ** 2 - x
