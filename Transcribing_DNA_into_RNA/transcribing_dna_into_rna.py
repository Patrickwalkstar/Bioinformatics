# See: http://rosalind.info/problems/rna/

import sys

# Open the file in read-only format
if len(sys.argv) == 1: 
    file = open('rosalind_rna.txt', mode='r')
else:
    file = open(sys.argv[1], mode='r')

# Read the first line of the file, the line that contains the DNA string
dnaString = file.readline().strip()

# Replace every instance of the character 'T' with the character 'U'
rnaString = dnaString.replace('T', 'U')

# Print the new string, the RNA string, where every 'T' is replaced by a 'U'
# Also print the original DNA string
print(f'DNA String: \n{dnaString} \n')
print(f'RNA String: \n{rnaString}')