# See: http://rosalind.info/problems/revc/

import sys 

# Open the file in read-only format, if the file is not used as a command line argument
# then open a file already in the same directory as the program.

if len(sys.argv) == 1: 
    file = open('rosalind_revc.txt', mode='r')
else:
    file = open(sys.argv[1], mode='r')

# Find the reverse complement of the input DNA string.
# The dnaString is read in and reversed (with [::-1], then A --> temp, T --> A, temp --> T
#                                                     then C --> temp, G --> C, temp --> G
# Temp is needed because if the replacement was A --> T, T --> A or C --> G, G --> C,
# then the values that are meant to stay as T or G after the first replacement would
# be replaced by A or C in the second round of replacements. Thus, we would be left with
# a string of As and Cs. Temp helps us remember which index values need to be replaced again.
# This is common practice in coding, when we "swap" multiple values in the same string.
reversed_line = file.readline()[::-1]
original_dnaString = reversed_line.replace('A', 'temp').replace('T', 'A').replace('temp', 'T')\
                                  .replace('C', 'temp').replace('G', 'C').replace('temp', 'G')

# Simply store the elements of the string in a list, and depending on their base, replace it with the complement.
# NOTE: Replacing values while iterating can be dangerous.
new_dnaString = list(reversed_line)
for index, base in enumerate(new_dnaString): 
    if base == 'A':
        new_dnaString[index] = 'T'
    elif base == 'T':
        new_dnaString[index] = 'A'
    elif base == 'C':
        new_dnaString[index] = 'G'
    elif base == 'G':
        new_dnaString[index] = 'C'

#Print the reverse complement of the original DNA string using the new method.
print(''.join(new_dnaString))


# Print the reverse complement of the original DNA string using the original method.
print(original_dnaString)