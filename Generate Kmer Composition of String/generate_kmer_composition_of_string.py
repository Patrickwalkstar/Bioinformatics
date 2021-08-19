# See: http://rosalind.info/problems/ba3a/

import sys

if len(sys.argv) == 1: 
    file = open('rosalind_ba3a.txt', mode='r')
else:
    file = open(sys.argv[1], mode='r')

lines = file.readlines()

k_length = int(lines[0].rstrip())
myseq = lines[1].rstrip()

def kmer_comp(sequence, k_length):
    kmers = []
    for i in range(len(sequence) - k_length + 1):
        kmers.append(sequence[i:i + k_length])
    return kmers

for i in kmer_comp(myseq, k_length):
    print(i)