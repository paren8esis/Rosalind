# The DNA codon table
DNA_codons = {'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V', 'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V', 'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V', 'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V', 'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A', 'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A', 'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A', 'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A', 'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D', 'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', 'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G', 'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G', 'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G' }

# Open file for reading
f = open('rosalind_splc.txt', 'r')

# Read DNA string and substrings
data = f.read().split('>')
s_list = []
for s in data:
	if (s != ''):
		newline = s.find('\n')
		s_list.append(s[newline:].replace('\n', ''))

DNA = s_list[0]
s_list = s_list[1:]

# Remove introns
for s in s_list:
	DNA = DNA.replace(s, '')

# Transcribe and translate into protein
start_codon = DNA.find('ATG')
protein = ''
for i in range(start_codon, len(DNA), 3):
	if ((DNA[i:i+3] == 'TAA') or (DNA[i:i+3] == 'TAG') or (DNA[i:i+3] == 'TGA')):
		break
	protein += DNA_codons[DNA[i:i+3]]

# Print result
print(protein)

# Close the file
f.close()
