def find_reverse_complement(s):
	''' Returns the reverse complement string of the given DNA string '''
	transtab = s.maketrans('ATCG', 'TAGC')
	return s.translate(transtab)[::-1]


def find_reverse_palindromes(s):
	''' Finds all the reverse palindromes of the given DNA string, 
			of size between 4 and 12. '''
	palindromes = []
	for length in range(4,13):
		for index in range(len(s)-length+1):
			if (s[index:index+length] == find_reverse_complement(s[index:index+length])):
				palindromes.append((index+1, length))
	return palindromes


# Open file for reading
f = open('rosalind_revp.txt', 'r')

# Read DNA string
DNA_str = f.read()
newline = DNA_str.find('\n')
DNA_str = DNA_str[newline:].replace('\n', '')

# Find the reverse palindromes
rev_palindromes = find_reverse_palindromes(DNA_str)

# Print results
for rev_palindrome in rev_palindromes:
	print(rev_palindrome[0], rev_palindrome[1])

# Close the file
f.close()
