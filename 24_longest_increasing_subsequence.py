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

def longest_increasing_subsequence(X, N):
	""" Returns the Longest Increasing Subsequence in the Given List """
	P = [0 for i in range(N)]
	M = [0 for i in range(N+1)]
	L = 0
	for i in range(N):
		lo = 1
		hi = L
		while lo <= hi:
			mid = (lo+hi)//2
			if (X[M[mid]] < X[i]):
				lo = mid+1
			else:
				hi = mid-1
 
		newL = lo
		P[i] = M[newL-1]
		M[newL] = i
 
		if (newL > L):
			L = newL
 
	S = []
	k = M[L]
	for i in range(L-1, -1, -1):
		S.append(X[k])
		k = P[k]       
	return S[::-1]

def longest_decreasing_subsequence(X, N):
	""" Returns the Longest Decreasing Subsequence in the Given List """
	P = [0 for i in range(N)]
	M = [0 for i in range(N+1)]
	L = 0
	for i in range(N):
		lo = 1
		hi = L
		while lo <= hi:
			mid = (lo+hi)//2
			if (X[M[mid]] > X[i]):
				lo = mid+1
			else:
				hi = mid-1
 
		newL = lo
		P[i] = M[newL-1]
		M[newL] = i
 
		if (newL > L):
			L = newL
 
	S = []
	k = M[L]
	for i in range(L-1, -1, -1):
		S.append(X[k])
		k = P[k]       
	return S[::-1]

# Open file for reading
f = open('rosalind_lgis.txt', 'r')

# Read number n and permutation p
data = f.read()
first_newline = data.find('\n')

n = int(data[:first_newline].strip('\n'))
p = [int(x) for x in data[first_newline+1:].strip('\n').replace('\n', ' ').split(' ')]

# Find longest increasing/decreasing subsequences
LIS = longest_increasing_subsequence(p, n)
LDS = longest_decreasing_subsequence(p, n)

# Print results
for el in LIS:
	print(el, end=' ')
print('\n', end='')
for el in LDS:
	print(el, end=' ')
print('\n', end='')

# Close the file
f.close()
