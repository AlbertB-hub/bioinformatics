f = open("10 Finding a Motif in DNA/rosalind_subs.txt")
stringDNA = f.readline().rstrip()
motif = f.readline().rstrip()

s = ""
#The program iterates each indices of stringDNA in search of
#the motif with a nested loop
for i in range(len(stringDNA)-len(motif) + 1):
    for j in range(len(motif)):
        s = s + stringDNA[i+j]
        if s == motif:
            print(i + 1, end = " ")
    s=""


