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
f = open('rosalind_iprb.txt', 'r')

# Read the k, m, n parameters
k, m, n = f.read().strip('\n').split(' ')
k = int(k)
m = int(m)
n = int(n)
total = float(k + m + n)

prob = ((k/total)*((k-1)/(total-1))) + ((k/total)*(m/(total-1))) + ((k/total)*(n/(total-1))) + ((m/total)*(k/(total-1))) + (((m/total)*((m-1)/(total-1)))*(3/4)) + (((m/total)*(n/(total-1)))*(1/2)) + ((n/total)*(k/(total-1))) + (((n/total)*(m/(total-1)))*(1/2))

print(prob)

# Close the file
f.close()

