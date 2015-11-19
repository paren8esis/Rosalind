# Open file for reading
f = open('rosalind_fibd.txt', 'r')

# Read the parameters
n, m = f.read().strip('\n').split(' ')
n = int(n)
m = int(m)

# Initialize list with rabbit categories 
# i.e. infants, 2-month-olds, 3-month-olds, ...
rabbit_cat = []
for i in range(0, m):
	rabbit_cat.append(0) 

# Compute growth of rabbit population
rabbit_cat[0] = 1
for i in range(1, n):
	infs = sum(rabbit_cat[1:])	# all the new infants
	rabbit_cat = [infs] + rabbit_cat[:-1]

# Print result
print(sum(rabbit_cat))

# Close the file
f.close()
