#Search how many time each k-mer appears in a given String. Returns a dictionary
 
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range( n - k+1):
        Pattern = Text[i:i+k]
        if Pattern in freq:
            freq[Pattern] += 1
        else:
            freq[Pattern] = 1
    return freq

k = 3
Text = "CGATATATCCATAG"

print(FrequencyMap(Text, k))