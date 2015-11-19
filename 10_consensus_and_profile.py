def initialize_matrix(s):
	''' Initializes the profile matrix with 4 rows of zeros '''
	profile = []
	for j in range(0,4):
		row = []
		for i in range(0, s):
			row.append(0)
		profile.append(row)
	return profile

def count_bases(profile, new_str):
	''' Checks the given DNA string and increments the corresponding 			
			counter in the profile matrix '''
	for i in range(0, len(new_str)):
		if (new_str[i] == 'A'):
			profile[0][i] += 1
		elif (new_str[i] == 'C'):
			profile[1][i] += 1
		elif (new_str[i] == 'G'):
			profile[2][i] += 1
		else:
			profile[3][i] += 1

	return profile

# Open file for reading
f = open('rosalind_cons.txt', 'r')

# Read the DNA strings and create the profile matrix
i = 0
new_str = ''
num_strings = 0
for line in f:
	if (line[0] == '>'):	# Label reached
		num_strings += 1
		if (new_str != ''):
			if (i == 0):	# First DNA string, initialize matrix
				profile = initialize_matrix(len(new_str))
				i = 1
			profile = count_bases(profile, new_str)
			new_str = ''
	else:
		new_str += line.strip('\n')

profile = count_bases(profile, new_str)

# Compute the consensus
consensus = ''
for i in range(0, len(profile[0])):
	max_row = max(profile, key=lambda x: x[i])
	if (profile.index(max_row) == 0):
		consensus += 'A'
	elif (profile.index(max_row) == 1):
		consensus += 'C'
	elif (profile.index(max_row) == 2):
		consensus += 'G'
	else:
		consensus += 'T'

# Print the consensus
print(consensus)

# Print the profile
print('A: ', end="")
for i in range(0, len(profile[0])):
	print(profile[0][i], end=" ")
print('\nC: ', end="")
for i in range(0, len(profile[1])):
	print(profile[1][i], end=" ")
print('\nG: ', end="")
for i in range(0, len(profile[2])):
	print(profile[2][i], end=" ")
print('\nT: ', end="")
for i in range(0, len(profile[3])):
	print(profile[3][i], end=" ")
print('\n')

# Close the file
f.close()
