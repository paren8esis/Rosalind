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
f = open('rosalind_fibd.txt', 'r')

# Read the parameters
n, m = f.read().strip('\n').split(' ')
n = int(n)
m = int(m)

# Initialize list with rabbit categories 
# i.e. infants, 2-month-olds, 3-month-olds, ...
rabbit_cat = []
for i in range(0, m):
	rabbit_cat.append(0) 

# Compute growth of rabbit population
rabbit_cat[0] = 1
for i in range(1, n):
	infs = sum(rabbit_cat[1:])	# all the new infants
	rabbit_cat = [infs] + rabbit_cat[:-1]

# Print result
print(sum(rabbit_cat))

# Close the file
f.close()
