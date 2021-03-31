#Order of genotypes and probabilities of having a dominant offspring
##AA-AA 1
#AA-Aa 1
#AA-aa 1
#Aa-Aa 0.75
#Aa-aa 0.5
#aa-aa 0
f = open("11 to 20/13 Calculating Expected Offspring/rosalind_iev.txt").read().split(" ")
#number of babies
n = 2

i = 0
while i < len(f):
    f[i]= float(f[i])
    i+=1


totalOff= (f[0]+f[1]+f[2]+f[3]*0.75+f[4]*0.5)*n
print(totalOff)