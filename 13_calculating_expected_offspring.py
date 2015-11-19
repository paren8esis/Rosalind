# Open file for reading
f = open('rosalind_iev.txt', 'r')

# Read the number of pairs for each category
AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa = f.read().strip('\n').split(' ')

# Calculate the expected value of the number offsprings with dominant allele
print((int(AA_AA)*2) + (int(AA_Aa)*2) + (int(AA_aa)*2) + (int(Aa_Aa)*(3/4)*2) + (int(Aa_aa)*(1/2)*2))

# Close the file
f.close()
