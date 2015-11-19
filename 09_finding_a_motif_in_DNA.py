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
f = open('rosalind_subs.txt', 'r')

# Read s and t
s = f.readline().strip('\n')
t = f.readline().strip('\n')

i = 0
while (i < len(s)):
	new_i = s[i:].find(t)
	if (new_i == -1):
		break
	print(new_i + i + 1, end=' ')
	i += new_i + 1

print('\n')

# Close the file
f.close()
