f = open("11 to 20/15 Calculating Protein Mass/rosalind_prtm.txt").read().strip()

mass= open("11 to 20/15 Calculating Protein Mass/Monoisotopic mass table.txt").read().replace("   ", " ").replace("\n"," ").strip().split(" ")
i = 0

massDict = {}
while i < len(mass):
    if i%2 == 0:
        massDict[mass[i]]=float(mass[i+1])
    i+=1

total = 0
for i in f:
    total = massDict.get(i)+total

print(total)
