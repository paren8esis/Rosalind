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

GC = {'C', 'G'}

# Open file for reading
f = open('rosalind_gc.txt', 'r')

data = []
curr = ''

# Read the data
for line in f:
	if ('>' in line):	# Keep only IDs
		if (curr != ''):
			data.append(curr)
			curr = ''
		data.append(line[-5:-1:])
	else:
		curr += line[:-1:]

if (curr != ''):
	data.append(curr)

# Calculate the highest GC-content
maxID = data[0]
maxGC = 0
for i in range(1,len(data),2):
	GC_cont = Counter(c for l in data[i] for c in l if (c in GC))
	if (round(((GC_cont['C'] + GC_cont['G'])/len(data[i]))*100, 6) > maxGC):
		maxGC = round(((GC_cont['C'] + GC_cont['G'])/len(data[i]))*100, 6)
		maxID = data[i-1]
	
print('Rosalind_' + maxID)
print(maxGC)

# Close the file
f.close()
