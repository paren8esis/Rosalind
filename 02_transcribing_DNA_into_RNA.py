# Open file for reading
f = open('rosalind_rna.txt', 'r')

# Read all the DNA data
dataDNA = f.read()

# Replace T with U
dataRNA = dataDNA.replace('T', 'U')

# Close the file
f.close()

# Print results 
print(dataRNA)

