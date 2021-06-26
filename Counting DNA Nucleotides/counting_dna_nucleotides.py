# See: http://rosalind.info/problems/dna/

# Open the file, in read-only format
file1 = open('../rosalind_dna.txt', 'r')

# Read the first line of the file, the line that contains the DNA string
dnaString = file1.readline()

# Initialize counts for each of the bases
A, C, G, T = 0, 0, 0, 0

# For each base in the input DNA string, if the base matches
# the appropriate character, increase that base's count.
for base in dnaString:
    if base == 'A':
        A += 1
    if base == 'C':
        C += 1
    if base == 'G':
        G += 1
    if base == 'T':
        T += 1

# Print the counts of all bases, separated by spaces
print(A,C,G,T)
