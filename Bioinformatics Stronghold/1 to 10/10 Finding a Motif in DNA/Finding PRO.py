f = open("10 Finding a Motif in DNA/rosalind_subs.txt")
s1 = f.readline().rstrip()
s2 = f.readline().rstrip()

for i in range(len(s1)):
    if s1[i:].startswith(s2):
        print (i+1, end = " ")