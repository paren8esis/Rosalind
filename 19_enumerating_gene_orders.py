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
