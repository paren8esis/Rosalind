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

from collections import Counter

nucleobases = {'A', 'C', 'G', 'T'}

# Open file for reading
f = open('rosalind_dna.txt', 'r')

# Read all the DNA data
dataDNA = f.read()

# Count occurences of letters A, C, G T
occurences = Counter(c for l in dataDNA for c in l if (c in nucleobases))

# Close the file
f.close()

# Print results for A, C, G, T respectively
print(occurences['A'], occurences['C'], occurences['G'], occurences['T'])


