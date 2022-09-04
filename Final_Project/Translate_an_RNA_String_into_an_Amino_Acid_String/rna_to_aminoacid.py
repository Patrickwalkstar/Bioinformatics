'''
Title: Translate an RNA string into an amino acid string
Description: Given an RNA pattern, return the translation
of the RNA pattern into an amino acid string Peptide
Author: Patrick Walker
Date: 9 November 2020

See: http://rosalind.info/problems/ba4a/
'''

import sys
import json

# Open the file containing the RNA string "pattern"
if len(sys.argv) == 1: 
    rna_file = open('rna.txt', mode='r')
else:
    rna_file = open(sys.argv[1], mode='r')

# Read the first and only line of the file, which is the RNA string,
# remove the newline character from the right enf of the line
rna_string = rna_file.readline().rstrip()

# Create a dictionary that contains genetic code, describing the translation
# of an RNA 3-mer (codon) into one of 20 different amino acids
with open('rna_codons.json', 'r') as rna_codons_file: 
    rnaCodons = json.load(rna_codons_file)

# Create an empty array to store the found codons
foundCodons = []

# Iterate through the rna string by codon (lengths of 3)
for i in range(0, len(rna_string), 3):

    # Store each codon, which will be the current nucleotide to third one after the current nucleotide.
    foundCodons.append(rna_string[i:i+3])

# First, find all the amino acid values for each codon and store them in a similarly ordered list.
# Then, join the amino acids into a final peptide string.
peptide = ''.join([rnaCodons[codon] for codon in foundCodons])

# Finally, strip "Stop" from the end of the peptide and print the resulting value. Also, print the original rna string.
print(f'RNA String: \n{rna_string} \n')
print('Peptide: \n{} \n'.format(peptide.rstrip('Stop')))