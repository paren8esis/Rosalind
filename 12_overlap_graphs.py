def find_edges(DNA_strings):
	edges = []

	for i in range(0, len(DNA_strings)):
		str1 = DNA_strings[i]
		for j in range(0, len(DNA_strings)):
			if (i == j):
				continue
			str2 = DNA_strings[j]
			if (str1[-3:] == str2[:3]):	# Substring found
				edges.append((str1, str2))

	return edges

# Open file for reading
f = open('rosalind_grph.txt', 'r')

# Read and save all data from file
labels = {}
DNA_strings = []

new_str = ''
new_lbl = ''
for line in f:
	if (line[0] == '>'):	# Label reached
		if (new_str != ''):
			labels[new_str] = new_lbl
			DNA_strings.append(new_str)
			new_str = ''
			new_lbl = line[1:].strip('\n')
		else:	# First label
			new_lbl = line[1:].strip('\n')
	else:
		new_str += line.strip('\n')

labels[new_str] = new_lbl	# The last string
DNA_strings.append(new_str)

# Find all possible (birectional) edges
edges = find_edges(DNA_strings)

# Print result
for edge in edges:
	print(''.join((labels[edge[0]], ' ', labels[edge[1]])))

# Close the file
f.close()
