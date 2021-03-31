f = open("2 Transcribing DNA into RNA/rosalind_rna.txt") #Open file with ADN chain
s = f.read()
print(s.replace("T", "U"))
