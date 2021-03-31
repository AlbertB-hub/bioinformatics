f = open("7 Counting Point Mutations/rosalind_hamm.txt")
#Separate both given strings of DNA into a list
strands = f.read().splitlines()
hamm = 0
#Iterate both strings at same time checking different symbols. +1 if they differ
for acid in range(len(strands[0])):
    if strands[0][acid] != strands[1][acid]:
        hamm +=1
print(hamm)
