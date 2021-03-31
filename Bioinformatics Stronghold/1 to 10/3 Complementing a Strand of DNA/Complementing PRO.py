f = open("3 Complementing a Strand of DNA/rosalind_revc.txt")
s = f.read()
print(s)
s = s.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
print(s)
