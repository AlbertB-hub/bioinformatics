import re
#Read file and clean it to make a workable list
f = open("11 Consensus and Profile/rosalind_cons.txt").read().replace("\n","")
strDNA = re.split(">Rosalind_\d*",f)
strDNA.pop(0)

#Start variables. i%j for iterating the matrix. listX for storing the values as asked
#And contX to compare them later to get the Cons String. 
i, j = 0, 0
listA, listC, listG, listT = [], [], [], []
contA, contC, contG, contT = 0, 0, 0, 0
# s is a string for the consensus string
s = ""

while i < len(strDNA[1]):
#Iterate string by string to check how many times repeats each kind of nucleotid in given position
# j = string i = position
    while j < len(strDNA):
        if strDNA[j][i] == "A":
            contA +=1
        elif strDNA[j][i] == "C":
            contC +=1
        elif strDNA[j][i] == "G":
            contG +=1
        elif strDNA[j][i] == "T":
            contT +=1
        j+=1
#Store those values as asked for the output and print them later
    listA.append(contA)
    listC.append(contC)
    listG.append(contG)
    listT.append(contT)
#Compare the counters and add the most repeated nucletid to the Consensus string
    if contA >= contC and contA >= contG and contA >= contT:
        s = s+ "A"
    elif contC >= contA and contC >= contG and contC >= contT:
        s = s + "C"
    elif contG >= contA and contG >= contC and contG >= contT:
        s = s + "G"
    elif contT >= contA and contT >= contG and contT >= contC: 
        s = s + "T"
#Reset counters to 0 to check the next position of nucleotids
    contA = 0
    contC = 0
    contG = 0
    contT = 0
    i+=1
    j=0
#ASKED OUTPUT
print(s)
print("A: " + " ".join(str(v) for v in listA))
print("C: " + " ".join(str(v) for v in listC))
print("G: " + " ".join(str(v) for v in listG))
print("T: " + " ".join(str(v) for v in listT))
