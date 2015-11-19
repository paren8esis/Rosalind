from itertools import permutations

# Open file for reading
f = open('rosalind_perm.txt', 'r')

# Read the integer
n = int(f.read().strip('\n'))

# Find all permutations
p = list(permutations(range(1, n+1)))

# Print results
print(len(p))
for permutation in p:
	for el in permutation:
		print(el, end=' ')
	print('\n', end='')

# Close the file
f.close()
