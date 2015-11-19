codons = {'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4, 'H': 2, 'I': 3, 'K': 2, 'L': 6, 'M': 1, 'N': 2, 'P': 4, 'Q': 2, 'R': 6, 'S': 6, 'T': 4, 'V': 4, 'W': 1, 'Y': 2}

# Open file for reading
f = open('rosalind_mrna.txt', 'r')

# Read protein string
prot = f.read().strip('\n')

# Calculate number of all possible RNA strings
num_str = 1
for amino_acid in prot:
	num_str = (num_str * codons[amino_acid]) % 1000000

# Take into account stop codons
num_str = (num_str * 3) % 1000000

# Print result
print(num_str)

# Close the file
f.close()
