# Open file for reading
f = open('rosalind_revc.txt', 'r')

# Read all the DNA data
dataDNA = f.read()

# Replace T with U and print results
reversedDNA = dataDNA[::-1]
print(reversedDNA.translate({ord('A'): 'T', ord('T'): 'A', ord('C'): 'G', ord('G'): 'C'}))

# Close the file
f.close()

