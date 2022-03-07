# See: http://rosalind.info/problems/hamm/

import sys

# Open the file in read-only format
if len(sys.argv) == 1: 
    file = open('rosalind_hamm.txt', mode='r')
else:
    file = open(sys.argv[1], mode='r')

# Read in the first and second DNA strings and assign them to variables.
s, t = file.readline().rstrip('\n'), file.readline().rstrip('\n')

# Iterate through each character of both input strings at the same time.
# Look at the same index of both strings, if they do not match, return 1, else 0.
character_difference_count = sum((1 if s[char] != t[char] else 0 for char in range(len(s))))
    
# Print the Hamming distance, the number of differences in symbols between the two input DNA strings.
print(character_difference_count)

