from collections import Counter

nucleobases = {'A', 'C', 'G', 'T'}

# Open file for reading
f = open('rosalind_dna.txt', 'r')

# Read all the DNA data
dataDNA = f.read()

# Count occurences of letters A, C, G T
occurences = Counter(c for l in dataDNA for c in l if (c in nucleobases))

# Close the file
f.close()

# Print results for A, C, G, T respectively
print(occurences['A'], occurences['C'], occurences['G'], occurences['T'])


