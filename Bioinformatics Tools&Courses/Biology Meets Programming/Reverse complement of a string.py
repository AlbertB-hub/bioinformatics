def ReverseComplement(Pattern):   
    return Reverse(Complement(Pattern))

def Reverse(Pattern):
    return Pattern[::-1]

def Complement(Pattern):
    basepairs = {"A":"T", "G":"C", "T":"A", "C":"G"}
    complement = ""
    for base in Pattern:
        complement += basepairs.get(base)
    return complement

s = "AAAACCCGGT"
print(ReverseComplement(s))