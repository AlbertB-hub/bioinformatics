def fib(n,k):
    if n < 2:
        return n
    else:
        return fib(n-1,k)+(fib(n-2,k)*k)

print(fib(35,3))
