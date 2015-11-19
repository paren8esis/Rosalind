import urllib.request
import re

motif = 'N[^P][ST][^P]'

def search_uniprot(url):
	# Open url and read FASTA information
	info = urllib.request.urlopen(url).read().decode()
	
	# Ignore label (first line of FASTA file)
	ind = info.find('\n')
	info = info[ind+1:]
	
	# Remove newlines
	info = info.replace('\n', '')

	# Search for the N-glycosylation motif: N{P}[ST]{P}
	regexp = re.compile(motif)
	locations = []
	found = 0
	match = regexp.search(info)
	offset = 0
	while (match != None):
		found = 1
		locations.append(match.start()+offset)
		offset += match.start()+1
		info = info[match.start()+1:]	
		match = regexp.search(info)

	return found, locations	


# Open file for reading
f = open('rosalind_mprt.txt', 'r')

# Read the UniProt IDs
ids = []
for line in f:
	ids.append(line.strip('\n'))

# Ask UniProt for information
for uniprot_id in ids:
	url = 'http://www.uniprot.org/uniprot/' + uniprot_id + '.fasta'
	found, locations = search_uniprot(url)
	if (found != 0):
		print('\n' + uniprot_id)
		for loc in locations:
			print(loc+1, end=" ")

print('\n')

# Close the file
f.close()
