# See: http://rosalind.info/problems/subs/

import sys

# Open the file in read-only format
if len(sys.argv) == 1: 
    file = open('rosalind_subs.txt', mode='r')
else:
    file = open(sys.argv[1], mode='r')

# Read in the first two lines of the file, the main DNA string
# and the DNA substring
s = file.readline().rstrip('\n')
t = file.readline().rstrip('\n')

# Find the indices where the substring appears in the main string.
# Loop through the main string and compare the substring to
# a similarly-sized section of the main string. If the substring
# matches the current section of the main string, have the current
# index i + 1 be a part of the final list. 0th index requires i + 1.
# The startswith function helps find the indices where the
# substring matches the main string.
res = [i + 1 for i in range(len(s)) if s.startswith(t, i)]

# Unpack and print the indices where the substring was found
print(*res)
