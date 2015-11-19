def is_substr(find, data):
	if (len(data) < 1 and len(find) < 1):
		return False
	for i in range(len(data)):
		if (find not in data[i]):
			return False
	return True


def LCS(data):
	substr = ''
	if (len(data) > 1 and len(data[0]) > 0):
		for i in range(len(data[0])):
			for j in range(len(data[0])-i+1):
				if (j > len(substr) and is_substr(data[0][i:i+j], data)):
					substr = data[0][i:i+j]
	return substr


# Open file for reading
f = open('rosalind_lcsm.txt', 'r')

# Read the DNA strings
str_list = []

i = 0
new_str = ''
for line in f:
	if (line[0] == '>'):	# Label reached
		if (new_str != ''):
			str_list.append(new_str)
			new_str = ''
	else:
		new_str += line.strip('\n')
			
str_list.append(new_str)

# Compute the longest common substring
print(LCS(str_list))

# Close the file
f.close()
