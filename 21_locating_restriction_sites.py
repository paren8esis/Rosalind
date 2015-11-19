# Copyright 2015 paren8esis
#
# This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#!/usr/bin/env python3

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
