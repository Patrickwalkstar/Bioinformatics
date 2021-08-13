# See: http://rosalind.info/problems/dna/

import sys

# Open the file, in read-only format
if len(sys.argv) == 1: 
    file = open('rosalind_dna.txt', mode='r')
else:
    file = open(sys.argv[1], mode='r')

# Read the first line of the file, the line that contains the DNA string
dnaString = file.readline()

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

# Print the counts of all bases, each to a new line.
print('A: {}\nC: {}\nG: {}\nT: {}\n'.format(A,C,G,T))
