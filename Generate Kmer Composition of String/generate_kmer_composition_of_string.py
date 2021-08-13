# See: http://rosalind.info/problems/ba3a/

import sys

if len(sys.argv) == 1: 
    file = open('rosalind_ba3a.txt', mode='r')
else:
    file = open(sys.argv[1], mode='r')

lines = file.readlines()

k = int(lines[0].rstrip())
myseq = lines[1].rstrip()

def kmer_comp(string, number):
    kmers = []
    for i in range(len(string) - number + 1):
        kmers.append(string[i:i+number])
    return kmers

for i in kmer_comp(myseq, k):
    print(i)