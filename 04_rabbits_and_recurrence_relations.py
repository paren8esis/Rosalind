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

def fibK(n, k):
	''' Calculates the number of rabbit pairs after n months.
			A pair of rabbits reaches reproduction age after one month.
			Every pair of reproduction-age rabbits produces a litter of k 
			rabbit pairs. 
			
			The population begins with one pair of newborn rabbits. '''
	if ((n == 0) or (n == 1) or (n == 2)):
		return 1
	return fibK(n-1, k) + (k * fibK(n-2, k))


# Open file for reading
f = open('rosalind_fib.txt', 'r')

# Read the parameters
for line in f:
	n, k = [int(i) for i in line.split()]

# Calculate and print result
print(fibK(n, k))

# Close the file
f.close()
