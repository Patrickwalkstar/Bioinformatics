# See: http://rosalind.info/problems/rna/

# Open the file in read-only format
file1 = open('../rosalind_rna.txt', 'r')

# Read the first line of the file, the line that contains the DNA string
dnaString = file1.readline()

# Replace every instance of the character 'T' with the character 'U'
rnaString = dnaString.replace('T', 'U')

# Print the new string, the RNA string, where every 'T' is replaced by a 'U'
print(rnaString)