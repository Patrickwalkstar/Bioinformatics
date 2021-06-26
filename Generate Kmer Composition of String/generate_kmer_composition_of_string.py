# See: http://rosalind.info/problems/ba3a/

myfile = open("../rosalind_ba3a.txt", "r")
myfile = myfile.readlines()

k = int(myfile[0].rstrip())
myseq = myfile[1].rstrip()

def kmer_comp(string, number):
    kmers = []
    for i in range(len(string) - number + 1):
        kmers.append(string[i:i+number])
    return kmers

for i in kmer_comp(myseq, k):
    print(i)