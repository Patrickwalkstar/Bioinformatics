'''
Title: Find Substrings of a Genome Encoding a Given Amino Acid String
Description: Given a DNA string and an amino acid string (peptide), return
all substrings of the DNA string that encode Peptide (if they exist).
Author: Patrick Walker
Date: 9 November 2020

See: http://rosalind.info/problems/ba4b/
'''

import sys

# A function that generates the reverse complement of a DNA string
def reverse_complement(dna):

    # Initialize a dictionary that stores the complement of each nucleotide
    complements = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}

    # In reverse, order: for every base in the dna string, find the complement -
    # the matching value in the dictionary. Then, join the complements.
    base_list = []
    for base in reversed(dna):
        base_list.append(complements[base])
    return ''.join(base_list)

# A function that translates the DNA string into a peptide using the codon table.
def translate(dna):

    # First check to see if the length of the dna is a multiple of 3, if not, then return nothing.
    if len(dna) % 3 != 0:
        return

    # If the length of the DNA string is a multiple of 3, then first, get the
    # codons (lengths of 3) and find their corresponding amino acids and add them to a temporary list.
    # Then, join the amino acids to form peptide.
    return ''.join([codon_table[dna[i:i+3]] for i in range(0, len(dna), 3)])

# Define a function that finds the substrings that encode for a given amino acid string.
def find_substrings_encoding_amino_acid(dna, peptide):

    # Find the reverse complement of the input DNA string
    reverse_complement_dna_string = reverse_complement(dna)

    # Find the necessary length of a substring
    k = len(peptide) * 3
    substrings = []

    # Loop through the sequnece based on different starting positions.
    for start in [0, 1, 2]:
        # Loop through forward sequence
        for i in range(start, len(dna), 3):
            substring = dna[i:i+k]
            if len(substring) != k:
                break
            if translate(substring) == peptide:
                substrings.append(substring)
        # Loop through reverse complement
        for i in range(start, len(reverse_complement_dna_string), 3):
            substring = reverse_complement_dna_string[i:i+k]
            if len(substring) != k:
                break
            # If substring is a match, append reverse complement of it so it matches original string
            if translate(substring) == peptide:
                substrings.append(reverse_complement(substring))

    #Return the list of substrings that result
    return substrings

# Open the file containing the DNA string and an amino acid string (Peptide)
if len(sys.argv) == 1: 
    dna_and_peptide_file = open('dna_string_and_amino_acid_string.txt', mode='r')
else:
    dna_and_peptide_file = open(sys.argv[1], mode='r')

# Read the first two lines of the file. The first line will contain the DNA string and
# the second line will contain the amino acid string, the peptide. Strip the newline
# characters from these lines.
dna_string = dna_and_peptide_file.readline().rstrip()
amino_acid_string = dna_and_peptide_file.readline().rstrip()

codon_table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
    }

for substring in find_substrings_encoding_amino_acid(dna_string, amino_acid_string):
    print(substring)
