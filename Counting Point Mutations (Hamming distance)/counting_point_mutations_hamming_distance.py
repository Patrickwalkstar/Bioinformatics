# See: http://rosalind.info/problems/hamm/

import sys

# Open the file in read-only format
if len(sys.argv) == 1: 
    file = open('rosalind_hamm.txt', mode='r')
else:
    file = open(sys.argv[1], mode='r')


# Read in the first and second DNA strings and assign them to variables.
# Also initialize a count to keep track of the number of differences.
s, t, count = file.readline().rstrip('\n'), file.readline().rstrip('\n'), 0

# Iterate through each character of both input strings at the same time.
# Look at the same index of both strings, if they do not match, increase the count.
for char in range(len(s)):
    if s[char] != t[char]:
        count += 1

# Print the Hamming distance, the number of differences in symbols between the two input DNA strings.
print(count)