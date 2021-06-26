# See: http://rosalind.info/problems/hamm/

# Open the file in read-only format
file1 = open('../rosalind_hamm.txt', 'r')

# Read in the first and second DNA strings and assign them to variables.
# Also initialize a count to keep track of the number of differences.
s, t, count = file1.readline().rstrip('\n'), file1.readline(), 0

# Iterate through each character of both input strings at the same time.
# Look at the same index of both strings, if they do not match, increase the count.
for char in range(len(s)):
    if s[char] != t[char]:
        count += 1

# Print the Hamming distance, the number of differences in symbols between the two input DNA strings.
print(count)