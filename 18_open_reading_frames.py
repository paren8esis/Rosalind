import re

trans = {'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V', 'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V', 'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V', 'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V', 'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A', 'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A', 'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A', 'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A', 'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D', 'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', 'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G', 'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G', 'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G' }

proteins = []

def find_reverse_DNA_string(s):
	''' Returns the reverse complement string of the given DNA string '''
	r = ''
	for letter in s:
		if (letter == 'A'):
			r += 'T'
		elif (letter == 'T'):
			r += 'A'
		elif (letter == 'C'):
			r += 'G'
		else:
			r += 'C'

	return r[::-1]

def translate_str(start, s):
	''' Takes as input a DNA string and the position of a start codon 
			and returns the translated protein string '''
	prot = ''
	for i in range(start, len(s), 3):
		if ((s[i:i+3] == 'TAA') or (s[i:i+3] == 'TAG') or (s[i:i+3] == 'TGA')):
			return prot
		prot += trans[s[i:i+3]]

	return ''

def compute_ORFs(s):
	''' Finds the position of all start codons of the given DNA string '''
	starts = []
	start_codon = re.compile('ATG')
	matches = re.finditer(start_codon, s)
	for match in matches:
		starts.append(match.start())
	
	for start in starts:
		prot = translate_str(start, s)
		if ((prot not in proteins) and (prot != '')):
			proteins.append(prot)
		

# Open file for reading
f = open('rosalind_orf.txt', 'r')

# Read DNA string
DNA_str = f.read()
newline = DNA_str.find('\n')
DNA_str = DNA_str[newline:].replace('\n', '')

# Find the reverse complement of the given DNA string
r_DNA_str = find_reverse_DNA_string(DNA_str)

# Find all candidate protein strings
compute_ORFs(DNA_str)
compute_ORFs(r_DNA_str)

# Print results
for protein in proteins:
	print(protein)

# Close the file
f.close()
