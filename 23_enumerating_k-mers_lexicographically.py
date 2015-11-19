from itertools import permutations, repeat

# Open file for reading
f = open('rosalind_lexf.txt', 'r')

# Read ordered alphabet and length of strings
alphabet = []
for line in f:
	line = line.strip('\n')
	if (line.isnumeric()):
		n = int(line)
	else:
		alphabet += line.split(' ')

# Find and print all possible substrings
perm_alph = [x for item in alphabet for x in repeat(item, n)]

perm = permutations(''.join(perm_alph), n)
subs = []
for p in perm:
	if (p not in subs):
		subs.append(p)

for s in subs:
	print(''.join(s))

# Close the file
f.close()
