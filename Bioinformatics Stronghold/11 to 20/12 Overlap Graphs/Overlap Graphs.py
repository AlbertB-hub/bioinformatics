import re
f = open("12 Overlap Graphs/rosalind_grph.txt").read().replace("\n","").replace(">","")

#Separate in two lists the values and the FASTA indices
listValues = re.split("Rosalind_\d*",f)
listValues.pop(0)
listKeys = re.findall("Rosalind_\d*",f)

#Overlap graph k
k = 3
i, j = 0, 0

#Just check the heads and the tails of the string for matches.
#Return the FASTA indices
#j != i is for avoiding to print the same string if it starts like it ends
while i < len(listValues):
    while j < len(listValues):
        if j != i and listValues[i][-k:] == listValues [j][:k]:
            print(listKeys[i], end = " ")
            print(listKeys[j])
        j +=1
    i+=1
    j=0

