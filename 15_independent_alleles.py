from math import factorial

def bernulli_prob(k, N):
	return (factorial(2**k)/(factorial(N)*factorial((2**k) - N)))*((1/4)**N)*((3/4)**((2**k) - N))

# Open file for reading
f = open('rosalind_lia.txt', 'r')

# Read parameters k and N
k, N = f.read().strip('\n').split(' ')
k = int(k)
N = int(N)

# Compute the probability
prob = 0.0
i = N
while (i <= (2**k)):
	prob += bernulli_prob(k, i)
	i += 1

# Print result
print(round(prob, 3))

# Close the file
f.close()
