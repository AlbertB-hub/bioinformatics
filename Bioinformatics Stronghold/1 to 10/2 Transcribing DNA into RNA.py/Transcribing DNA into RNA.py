f = open("2 Transcribing DNA into RNA/rosalind_rna.txt") #Open file with DNA chain
toString = f.read()
transcription = ""

for c in toString:
    if c == "T":
        transcription=transcription + "U"
    else:
        transcription = transcription + c
print(toString)
print(transcription)
