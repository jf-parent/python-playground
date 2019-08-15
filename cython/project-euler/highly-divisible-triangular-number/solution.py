def count_factor(n):
    factor_count = 0
    i = 1
    while i*i < n:
        if n % i == 0:
            factor_count += 2
        i += 1

    if i*i == n:
        factor_count += 1

    return factor_count

def get_triangular_number(n):
    return (n*(n+1))/2

t=1
while True:
    factor_count = count_factor(get_triangular_number(t)) 
    if t%100==0:
        print(t,factor_count)

    if factor_count >= 500:
        break

    t+=1
print(get_triangular_number(t))
