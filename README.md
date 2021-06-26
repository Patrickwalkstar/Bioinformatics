# Bioinformatics
 the practice of bioinformatics concepts


### Complementing a Strand of DNA

Find the reverse complement of a DNA string - the complementary strand.

``input:`` a DNA string _s_ of length at most 1000 bp (base pairs).

``ouput:`` the reverse complement _s<sup>c</sup>_ of _s_.

[Link to the problem](http://rosalind.info/problems/revc/)

### Compute GC Content

Identify unknown DNA quickly by computing the GC-content of a DNA string.

``input:`` at most 10 strings of DNA in FASTA format (of length at most 1kbp)

``ouput:`` the ID of the string having the highest GC-content, the GC-content of that string within 0.001 absolute error.

**Fasta Format**: A text format used for naming genetic strings in databases. See link directly below.

[Link to the problem](http://rosalind.info/problems/gc/)

### Construct a De-Bruijn Graph of a Collection of k-mers

With a collection of k-mers, form an adjacency list (that represents a De-Buijn graph). This list can be used to reconstruct possible DNA strings.

``input:`` a collection of k-mers *Patterns*

``ouput:`` the de-bruijn graph, in the form of an adjacency list (a list that shows directly adjacent-connected nodes, which are overlapping 3-mers)

Here, prefixes -> suffixes (for kmer GAGG, prefix GAG -> suffix AGG, because AGG exists in our suffixes) and (for kmer CAGG, prefix CAG -> AGG, AGG again, becuase CAGG appears twice in our collection.)

**De-bruijn Graph**: a graph to show the connectedness of the kmers in the input collection. [ref](https://en.wikipedia.org/wiki/De_Bruijn_graph)

[Link to the problem](http://rosalind.info/problems/ba3e/)

### Construct a De-Bruijn Graph of a String

With a set kmer length, determine the constructed debruijn graph, in the form of an adjacency list, from a DNA string.

``input:`` an integer *k* and a *genome DNA string*

``ouput:`` a de-bruijn graph (with *k* overlap), in the form of an adjacency list (a list that shows the overlapping, directly adjacent-connected nodes, a list containing the edges of the graph)

For example: if the integer *k* is 4, the resulting adj-list will show (Node -> Node) like (AAG -> AGA), where the rightmost AG of the first node overlaps with the leftmost AG from the second node

[Link to the problem](http://rosalind.info/problems/ba3d/)

### Construct the Overlap Graph of a Collection of k-mers

With a collection of *Patterns* of *k*-mers, create an overlap graph in the form of an adjacency list. The length *k* is the length of any of the kmers in the input collection.

``input:`` a collection *Patterns* of *k*-mers

``ouput:`` the overlap graph from the given patterns, in the form of an adjacency list

**Overlap Graph**: Here, the overlap graph is constructed dependending on which kmer nodes are overlapping, hence the name. The overlapping length of the kmer is *k*-1. For exmaple: kmer CATGC -> ATGCG, because the ATGC from the right side of the first kmer node overlaps with the ATGC from the left side of the second kmer node.

[Link to the problem](http://rosalind.info/problems/ba3c/)

### Counting DNA Nucleotides

Determine the count of nucleobases in a string of DNA. ("A", "C", "G", "T" in a string of DNA). The beginnings of quantitative analysis for the genome, and several strings of DNA.

``input:`` a DNA string *s* of length at most 1000 nt (nucleotides)

``output:`` four integers (sep. by spaces) counting the respective number of times that the symbols "A", "C", "G", "T" occur in *s*.

[Link to the problem](http://rosalind.info/problems/dna/)

### Counting Point Mutations (Hamming Distance)

[Link to the problem](http://rosalind.info/problems/hamm/)

### Final Project



[Final Report](https://docs.google.com/document/d/1nkJ5C9Zq09Mcz4FYCfPWDgldojZAyiPSiqjrAu53UmU/edit?usp=sharing), 
[Presentation](https://docs.google.com/presentation/d/1ECVJqK5J4FRt5dRepjg3AS8YTQGWmXU1HvhFJ0exazQ/edit?usp=sharing)

* #### Find Substrings of a Genome Encoding a Given Amino Acid String

[Link to the problem](http://rosalind.info/problems/ba4b/)

* #### Translate an RNA String into an Amino Acid String

[Link to the problem](http://rosalind.info/problems/ba4a/)

### Finding a Motif in DNA

[Link to the problem](http://rosalind.info/problems/subs/)

### Generate K-mer Composition of a String

[Link to the problem](http://rosalind.info/problems/ba3a/)

### Reconstruct a String from its Genome Path

[Link to the problem](http://rosalind.info/problems/ba3b/)

### Transcribing DNA into RNA

[Link to the problem](http://rosalind.info/problems/rna/)