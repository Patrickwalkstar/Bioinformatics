# See: http://rosalind.info/problems/ba3a/

import sys

if len(sys.argv) == 1: 
    file = open('rosalind_ba3a.txt', mode='r')
else:
    file = open(sys.argv[1], mode='r')

lines = file.readlines()

k_length = int(lines[0].rstrip())
myseq = lines[1].rstrip()

# Return a list of kmers
def kmer_comp(sequence, k_length):
    return [sequence[i:i + k_length] for i in range(len(sequence) - k_length + 1)]

for i in kmer_comp(myseq, k_length):
    print(i)