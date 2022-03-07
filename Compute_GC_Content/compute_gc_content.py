# See: http://rosalind.info/problems/gc/

# The operator module exports a set of efficient
# functions corresponding to the intrinsic operators of Python
# The sys module provides access to some variables used or maintained 
# by the interpreter and to functions that interact with the interpreter
import operator, sys

# Function highestGCContent that inputs a text file with FASTA format DNA strings
# and returns a FASTA formatted DNA string with the highest GC content.
def highestGCContent(fasta):

    # Function fasta_r that parses and reads the input FASTA formatted DNA strings.
    # This function will only be used in the function highestGCCount, so its placement
    # within this file is appropriate.

    # Note: the yield statement suspends a function's execution and sends a value back
    # to the caller, but retains enough state to enable the function to resume where it is left off.
    # When resumed, the function continues execution immediately after the last yield run. This
    # allows its code to produce a series of values over time rather than computing them once
    # and sending back like a list.
    def fasta_r(fp):
        name = None
        seq = []
        # Read all the lines in the file
        for line in fp:
            line = line.rstrip()
            if line.startswith(">"):
                if name: yield name, ''.join(seq)  # interim genes
                name = line  # first name
                seq = []  # first seq
            else:
                seq.append(line)
        if name: yield name, ''.join(seq) # yields last gene

    genes = {}

    # Use the input file to read each of the FASTA formatted DNA strings.
    # Use the fasta_r function to read and store every DNA string.
    with open(fasta) as fp:
        for name, seq in fasta_r(fp):
            genes[name] = seq
    gc_in_genes = {}

    # For every gene in our dictionary of genes, count the G and C content,
    # and calculate the percentage of the gene that is G or C. Store the percentage.
    for gene in genes:
        gcSum = genes[gene].count('G') + genes[gene].count('C')
        percentage = (gcSum / len(genes[gene])) * 100
        gc_in_genes[gene] = percentage

    # Sort the dictionary by the first item, the percentage of gc content in the gene
    # (yes, this can be done), and return the 0th index of the newly formed list of sorted values,
    # the index where the gc content will be the highest.
    sortedByGC = sorted(gc_in_genes.items(), key=operator.itemgetter(1), reverse=True)
    return (sortedByGC[0])

# Find the DNA string, in FASTA format, with the highest GC content, percentage.
# Use the highestFCContent function above.


if len(sys.argv) == 1: 
    highestGCid = highestGCContent('rosalind_gc.txt')
else:
    highestGCid = highestGCContent(sys.argv[1])


# Format and print the results: the id without >, and the percentage with 6 decimal places exactly.
print(highestGCid[0].lstrip(">"))
print(format(highestGCid[1], '.6f'))

