# Open file for reading
f = open('rosalind_iprb.txt', 'r')

# Read the k, m, n parameters
k, m, n = f.read().strip('\n').split(' ')
k = int(k)
m = int(m)
n = int(n)
total = float(k + m + n)

prob = ((k/total)*((k-1)/(total-1))) + ((k/total)*(m/(total-1))) + ((k/total)*(n/(total-1))) + ((m/total)*(k/(total-1))) + (((m/total)*((m-1)/(total-1)))*(3/4)) + (((m/total)*(n/(total-1)))*(1/2)) + ((n/total)*(k/(total-1))) + (((n/total)*(m/(total-1)))*(1/2))

print(prob)

# Close the file
f.close()

