import re

f = open("1 to 10/6 Computing GC Content/rosalind_gc.txt")
dictTax = dict()
s = f.read()
#Depurate imported txt to make it more easy to handle
s2 = s.replace("\n", "")
s2 = s2.replace(">","")

#Create to lists for further elaboration of a dict
listaValues = re.split("Rosalind_\d{4}", s2)
listaValues.pop(0) #re.split returns an empty string "" in [0]. Pop it
listaKeys = re.findall("Rosalind_\d{4}", s2)

#Join values in a single dictionary. ID is kay and the DNA strin is the Value
for i in range(len(listaKeys)):
    dictTax[listaKeys[i]]=listaValues[i]

#GC content function calculator
def gcContent (chain):
    count = 0
    for c in chain:
        if c == "C" or c == "G":
            count +=1
    percent = count/len(chain)*100
    return percent

#comparator funcion. Returns max value of GC content in the dictionary
def comparator(dic):
    comp = 0
    key = "" 
    for k in dic.keys():
        if gcContent(dictTax[k]) > comp:
            comp = gcContent(dictTax[k])
            key = k
    print(k)
    return comp

print(comparator(dictTax))