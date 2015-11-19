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
