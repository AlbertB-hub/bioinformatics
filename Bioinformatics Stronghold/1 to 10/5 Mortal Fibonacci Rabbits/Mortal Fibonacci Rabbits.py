def fibo (n, m):
    #Start list this way to save lines of code an iterations
    fiboList = [1,1]
    for i in range(2, n):
    #For n<m Fibonacci keeps unaltered
        if len(fiboList) <m:
            fiboList.append(fiboList[-1]+fiboList[-2])
    #For n=m dies the first rabbit
        elif len(fiboList) == m:
            fiboList.append(fiboList[-1]+fiboList[-2]-1)
    #Rabbits keep dying following this formula Fn=Fn-1+Fn-2-F(n-(m+1))
        elif len(fiboList) >= m:
            fiboList.append(fiboList[-1]+fiboList[-2]-fiboList[-(m+1)])
            print(fiboList)
    return fiboList[-1]

print(fibo(90,3))
