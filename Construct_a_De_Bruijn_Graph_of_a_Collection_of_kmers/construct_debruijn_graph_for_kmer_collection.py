# See: http://rosalind.info/problems/ba3e/

import sys

# Initialize and open a file that contains a collection of kmer patterns
if len(sys.argv) == 1: 
    file = open('rosalind_ba3e.txt', mode='r')
else:
    file = open(sys.argv[1], mode='r')

kmers_list = file.read().split()

# First sort the input list of kmers
kmers_list.sort()

# Merge the prefix and suffix set in case there are single isolated edges. (can't be reached)
kmers = [k[:-1] for k in kmers_list] + [k[1:] for k in kmers_list]
kmers.sort()

# Generate nodes by iterating across our new list of kmer patterns.
nodes = {}
for index in range(len(kmers)):
    nodes[index] = kmers[index]

# Set up our set_nodes so that each non-identical kmer is numbered
# and its number is its previously defined index
set_nodes = {variable: kindex for kindex, variable in nodes.items()}

# Initialize a dictionary of deBG edges
edgeKmers = {}

# For every pattern in our list of kmer patterns:
# Initialize a prefix (first to second to last values)
# and suffix pattern (second to last values)
for kmerPattern in kmers_list:
    prefixPattern = kmerPattern[:len(kmerPattern) - 1]
    suffixPattern = kmerPattern[1:]

    # If the prefix pattern is already in our dictionary of edges,
    # append the suffix pattern to its "to" values
    if set_nodes[prefixPattern] in edgeKmers:
        edgeKmers[set_nodes[prefixPattern]].append(set_nodes[suffixPattern])

    # Since the prefix is not in in the dictionary, initialize it as a key,
    # and the suffix pattern as the first value in its list of "to" values
    else: #Notice: duplicates are allowed
        edgeKmers[set_nodes[prefixPattern]] = [set_nodes[suffixPattern]]

# Print each kmer pattern and its mapped to kmer patterns, joined together by commas.
# This returns a DeBruijn graph in the form of a printed adjacency list.
for fromkmer, tokmers in edgeKmers.items():
    print(nodes[fromkmer], '->', ','.join([nodes[tokmersVals] for tokmersVals in tokmers]))



