n = 35
k = 3

serie = [1, 1, 4]
for i in range(2, n-1):
    #Formula is F=Fn-1 + Fn-2*k
    serie.append(serie[-1] + serie[-2]*k)

print(serie)
print(serie[-1])
