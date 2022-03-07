# See: http://rosalind.info/problems/ba3b/

import sys

# Initialize the final DNA string
dnaString = ''

if len(sys.argv) == 1: 
    file = open('rosalind_ba3b.txt', mode='r')
else:
    file = open(sys.argv[1], mode='r')

# Use the input file as reference to "fill" the string
with file as f:

    # Append each line's first character
    # to the final DNA string.
    for line in f:
        dnaString = dnaString + line[0]

    # Because the last line in the file is the last line read,
    # it can be referenced here.
        # the last line's 1st (2nd) through last char
        # are appended to the final DNA string
    dnaString = dnaString + line[1:len(line)]

# Print the final DNA string
print(dnaString)