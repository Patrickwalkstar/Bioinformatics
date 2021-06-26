# See: http://rosalind.info/problems/revc/

# Open the file in read-only format
file1 = open('../rosalind_revc.txt', 'r')

# Find the reverse complement of the input DNA string.
# The dnaString is read in and reversed (with [::-1], then A --> temp, T --> A, temp --> T
#                                                     then C --> temp, G --> C, temp --> G
# Temp is needed because if the replacement was A --> T, T --> A or C --> G, G --> C,
# then the values that are meant to stay as T or G after the first replacement would
# be replaced by A or C in the second round of replacements. Thus, we would be left with
# a string of As and Cs. Temp helps us remember which index values need to be replaced again.
# This is common practice in coding, when we "swap" multiple values in the same string.
dnaString = file1.readline()[::-1].replace('A', 'temp').replace('T', 'A').replace('temp', 'T')\
                                  .replace('C', 'temp').replace('G', 'C').replace('temp', 'G')

# Print the reverse complement of the original DNA string.
print(dnaString)