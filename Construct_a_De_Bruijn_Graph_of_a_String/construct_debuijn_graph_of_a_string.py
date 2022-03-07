# See: http://rosalind.info/problems/ba3d/

import sys

# Initialize and open a file that contains an integer k and a genome text string

if len(sys.argv) == 1: 
    file1 = open('rosalind_ba3d.txt', mode='r')
else:
    file1 = open(sys.argv[1], mode='r')

# Initialize integer k and the genome text string
k = int(file1.readline())
text = file1.readline()

# Create and output a DeBruijn graph based
# on the input text and integer k.

# Initialize a list that will store the node k-1mers
k_minus_1mers = []

# Get the unique k-1 kmers, the nodes of the De Bruijn Graph
for i in range(len(text) - k + 2):
    k_minus_1mers.append(text[i:i + k - 1])

# Sort the list of k-1mers
k_minus_1mers.sort()

# Generate nodes the nodes by enumerating across our list of kmers.
nodes = {}
for index, variable in enumerate(k_minus_1mers):
    nodes[index] = variable

# Set up our set_nodes so that each non-identical kmer is numbered
set_nodes = {variable: index for index, variable in nodes.items()}

# Add edges based on the overlapping of our k-1 mers
edgeKmers = {}
for i in range(len(text) - k + 1):  # As indicated by the directions
    prefix = text[i:i + k - 1]
    suffix = text[i + 1:i + k]
    # Check to see if the "from" node (the prefix) already exists in our edges dictionary,
    # if it does, append the "to" value (the suffix) to the "from"'s list of values, else,
    # start a list of suffix values for the "from" kmer that starts with this first "to" kmer.
    if set_nodes[prefix] in edgeKmers:
        edgeKmers[set_nodes[prefix]].append(set_nodes[suffix])
    else:
        edgeKmers[set_nodes[prefix]] = [set_nodes[suffix]]

# Print each kmer and its mapped to values, sorted and joined together by commas.
# This returns a DeBruijn graph in the form of a printed adjacency list.
for fromkmers, tokmers in edgeKmers.items():
    print(nodes[fromkmers], '->', ','.join(sorted([nodes[tokmerVal] for tokmerVal in tokmers])))


file = open("rosalind_ba3d.txt", "r")
num = int(file.readline())
DNAstring = file.readline()

kmerdict = {}
kmerlength = len(DNAstring) - num + 1

for i in range(kmerlength):
    temp = DNAstring[i:i+num]
    if temp[0:num-1] not in kmerdict:
        kmerdict[temp[0:num-1]] = temp[1:num]
    else:
        kmerdict[temp[0:num-1]] += ', '+ temp[1:num]

for item in kmerdict:
    print(item+ " -> "+ kmerdict[item])