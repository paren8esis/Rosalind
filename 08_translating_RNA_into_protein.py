# Open file for reading
f = open('rosalind_prot.txt', 'r')

# The RNA codon table
codon_t = {'UUU': 'F', 'UUC': 'F' , 'CUU': 'L', 'AUU': 'I', 'GUU': 'V', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V', 'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V', 'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V', 'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A', 'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A', 'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A', 'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A', 'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D', 'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D', 'UAA': '', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E', 'UAG': '', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', 'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G', 'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G', 'UGA': '', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G', 'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G' }

# Read the mRNA string
mRNA = f.read().strip('\n')

# Find the start of the translation
start = mRNA.find('AUG')

# Cut the bases before the start
mRNA = mRNA[start:]

# Translation
prot = ''
for i in range(0, len(mRNA)-3, 3):
	prot += codon_t[mRNA[i:i+3]]
	if (codon_t[mRNA[i:i+3]] == ''):
		break

# Print protein string
print(prot)

# Close the file
f.close()

