# BioSeq Python Class

This Python script defines a `BioSeq` class for working with DNA sequences. The class provides methods for sequence validation, random sequence generation, nucleotide frequency calculation, transcription, DNA complement, reverse complement, GC content calculation, translation, generating reading frames, and identifying open reading frames (ORFs) that may encode proteins.

## Table of Contents
- [Usage](#usage)
  - [Initialization](#1-initialization)
  - [Random Sequence Generation](#2-random-sequence-generation)
  - [Nucleotide Frequency](#3-nucleotide-frequency)
  - [Transcription](#4-transcription)
  - [Complement and Reverse Complement](#5-complement-and-reverse-complement)
  - [GC Content](#6-gc-content)
  - [Translation](#7-translation)
  - [Open Reading Frames (ORFs)](#8-open-reading-frames-orfs)
- [Note](#note)

## Usage

### 1. Initialization
You can create a `BioSeq` object by providing a DNA sequence, sequence type (default is DNA), and an optional label. If the provided sequence is not a valid DNA sequence, an assertion error will be raised.

\\\python
my_sequence = BioSeq(seq="ATCGGCTA", seq_type="DNA", label="Example DNA")
\\\
### 2. Random Sequence Generation
Use the generate_random_DNA method to generate a random DNA sequence of a specified length.

\\\python
my_sequence.generate_random_DNA(length=20)

### 3. Nucleotide Frequency
Obtain the frequency of each nucleotide in the sequence using the nuc_freq method.


\\\python
frequency = my_sequence.nuc_freq()

### 4. Transcription
Convert a DNA sequence to its corresponding RNA sequence by replacing T with U using the transcription method.

\\\python
rna_sequence = my_sequence.transcription()

### 5. Complement and Reverse Complement
Get the DNA complement or reverse complement of the sequence using the DNA_complement and reverse_complement methods.


\\\python
complement = my_sequence.DNA_complement()
rev_complement = my_sequence.reverse_complement()

### 6. GC Content
Calculate the GC content of the sequence using the calculate_gc method.


\\\python
gc_content = my_sequence.calculate_gc()

### 7. Translation
Translate the DNA or RNA sequence into amino acids using the translate method.

\\\python
amino_acids = my_sequence.translate()

### 8. Open Reading Frames (ORFs)
Identify all possible proteins for all open reading frames using the orfs_poly_peptides method.


\\\python
orfs = my_sequence.orfs_poly_peptides()
