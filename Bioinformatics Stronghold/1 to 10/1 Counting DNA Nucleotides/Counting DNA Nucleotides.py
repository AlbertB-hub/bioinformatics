f = open("1 Counting DNA Nucleotides/rosalind_dna.txt") #Import file
strand = f.read()          #Initialize the strings
a = g = t = c = 0          #and the variables
error = 0
for nucl in strand:        #Iterate through the strand
    if nucl == "A":        #For each match, sum 1 to the corresponding counter
        a+=1
    elif nucl == "G":
        g+=1
    elif nucl == "T":
        t+=1
    elif nucl == "C":
        c+=1
    else:
        error = nucl

print(str(a) + " " + str(c) + " " + str(g) + " " + str(t))  #Print everything
print(error)
