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

# Open file for reading
f = open('rosalind_hamm.txt', 'r')

# Read the DNA strings
str1, str2 = f.read().strip('\n').split('\n')

# Compute the hamming distance between the two strings
hamm_dist = sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))

# Print the result
print(hamm_dist)

# Close the file
f.close()

