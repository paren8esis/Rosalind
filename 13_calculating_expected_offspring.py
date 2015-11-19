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
f = open('rosalind_iev.txt', 'r')

# Read the number of pairs for each category
AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa = f.read().strip('\n').split(' ')

# Calculate the expected value of the number offsprings with dominant allele
print((int(AA_AA)*2) + (int(AA_Aa)*2) + (int(AA_aa)*2) + (int(Aa_Aa)*(3/4)*2) + (int(Aa_aa)*(1/2)*2))

# Close the file
f.close()
