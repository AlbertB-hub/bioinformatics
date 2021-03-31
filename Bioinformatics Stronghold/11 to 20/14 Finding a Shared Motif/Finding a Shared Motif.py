import re

f = open("11 to 20/14 Finding a Shared Motif/rosalind_lcsm.txt").read().replace("\n","").replace(">","")

listValues = re.split("Rosalind_\d*",f)
listValues.pop(0)
listValues.sort()

l = len(listValues[0])
i = 0
j = 1
check = True

while l > 0:
    while i < len(listValues[0]):
        check = True
        if i+l <= len(listValues[0]):
            while j < len(listValues):                
                if listValues[0][i:i+l] in listValues[j]:
                    check = True
                else:
                    check = False
                    break
                j+=1                                    
            if check:
                print(listValues[0][i:i+l])
                break            
        else:
            break
        i+=1
        j=1        
    if check and i+l < len(listValues[0]):
        break
    l-=1
    i=0

