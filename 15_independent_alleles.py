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

from math import factorial

def bernulli_prob(k, N):
	return (factorial(2**k)/(factorial(N)*factorial((2**k) - N)))*((1/4)**N)*((3/4)**((2**k) - N))

# Open file for reading
f = open('rosalind_lia.txt', 'r')

# Read parameters k and N
k, N = f.read().strip('\n').split(' ')
k = int(k)
N = int(N)

# Compute the probability
prob = 0.0
i = N
while (i <= (2**k)):
	prob += bernulli_prob(k, i)
	i += 1

# Print result
print(round(prob, 3))

# Close the file
f.close()
