f = open("3 Complementing a Strand of DNA/rosalind_revc.txt")
s = f.read()
trad = ""
for c in s:
    if c == "A":
        trad = "T" + trad
    elif c == "T":
        trad = "A" + trad
    elif c == "C":
        trad = "G" + trad
    elif c == "G":
        trad = "C" + trad

print(s)
print(trad)

f2 = open("3 Complementing a Strand of DNA/solucion.txt", "w+")
f2.write(trad)
