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
