def fibK(n, k):
	''' Calculates the number of rabbit pairs after n months.
			A pair of rabbits reaches reproduction age after one month.
			Every pair of reproduction-age rabbits produces a litter of k 
			rabbit pairs. 
			
			The population begins with one pair of newborn rabbits. '''
	if ((n == 0) or (n == 1) or (n == 2)):
		return 1
	return fibK(n-1, k) + (k * fibK(n-2, k))


# Open file for reading
f = open('rosalind_fib.txt', 'r')

# Read the parameters
for line in f:
	n, k = [int(i) for i in line.split()]

# Calculate and print result
print(fibK(n, k))

# Close the file
f.close()
