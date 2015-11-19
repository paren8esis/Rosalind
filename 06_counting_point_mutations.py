# Open file for reading
f = open('rosalind_hamm.txt', 'r')

# Read the DNA strings
str1, str2 = f.read().strip('\n').split('\n')

# Compute the hamming distance between the two strings
hamm_dist = sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))

# Print the result
print(hamm_dist)

# Close the file
f.close()

