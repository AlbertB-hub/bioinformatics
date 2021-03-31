f = open("7 Counting Point Mutations/rosalind_hamm.txt")
s1 = f.readline()
s2 = f.readline()

print(sum([a != b for a, b in zip(s1, s2)]))