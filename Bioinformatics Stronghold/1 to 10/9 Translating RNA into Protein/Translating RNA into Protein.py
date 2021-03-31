mRNA = open("9 Translating RNA into Protein/rosalind_prot.txt").read()
codonList = open("9 Translating RNA into Protein\codon table").read().replace("      "," ").replace("   "," ").replace("\n", " ").split(" ")
i = 1
#print(codonList)
tripList = []
aminoList = []

#create lists of aminoacids and its corresponding mRNA
while i < (len(codonList)):
  tripList.append(codonList[i-1])
  aminoList.append(codonList[i])
  i += 2
#Iterate over the input mRNA. Use function to break all loops at once
def translator():
  s = ""
  prot = ""
  for i in range(len(mRNA)):
    s = s + mRNA[i]
#Check three by three nucleotids
    if len(s) == 3:
      for j in range(len(tripList)):
#If the three nucleotids are in the aminoList, check first if it is not a Stop.
#If it is a Stop, print the existing protein string and break the function.
#else add the corresponding aminoacid to the protein string 
        if s == tripList[j]:
          if s == "UAA" or s == "UAG" or s == "UGA":                       
            print(prot)
            return print("Stop reached") 
          else:
            prot = prot + aminoList[j]
            continue
#reset s string for next three nucleotids
      s = ""

translator()





    
