# See: http://rosalind.info/problems/ba3c/

# Initialize and open a file with a collection of kmer Patterns
file1 = open("../rosalind_ba3c.txt", 'r')

# Initialize and populate a list of patterns of kmers
kmers = file1.read().split()

#Initialize a list of adjacent overlapping kmer patterns
listValues = []

# Loop through the same list of kmers twice,
# comparing every kmer in the first version to each kmer in the second.
# As long as the kmer patterns are not the same, and there is overlap, add the
# overlapping pairs (as tuples) to a list.
for value1 in kmers:
    for value2 in kmers:
        if value1 != value2:
            # The overlapping region is the second nucleotide to the last of the first pattern,
            # compared to the first nucleotide to the second to last of the second pattern.
            if value1[1:len(value1)] == value2[:len(value2)-1]:
                listValues.append((value1, value2))

# Sort the list of kmer pattern overlaps by the first kmer in each tuple
sortedValues = sorted(listValues, key=lambda x: x[0])

# Print out all the overlap values in the form of an adjacency list
for value in sortedValues:
    print(value[0], '->', value[1])