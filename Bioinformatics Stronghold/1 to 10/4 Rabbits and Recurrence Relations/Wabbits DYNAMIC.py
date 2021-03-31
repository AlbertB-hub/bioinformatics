fibocache = {}
def fibo(n,k):
    if n == 2 or n == 1:
        return 1
    if (n,k) not in fibocache:
        fibocache[(n,k)] = fibo(n-1,k) + fibo(n-2,k) * k
    return fibocache[(n,k)]

print ( fibo( 33, 3) )
