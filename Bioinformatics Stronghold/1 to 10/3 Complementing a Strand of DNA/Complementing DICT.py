f = open("3 Complementing a Strand of DNA/rosalind_revc.txt")
s = f.read().rstrip()
complement = { "A" : "T", "T" : "A", "C" : "G", "G" : "C"}
result = []
for i in s[::-1]:
    result.append(complement[i])

print ("".join(result))
