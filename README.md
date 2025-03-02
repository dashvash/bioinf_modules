# modules_new
Classes for processing biosequences and function filter_fastq

## Description
### classes DNASequence, RNASequence, and AminoAcidSequence 

#### Availiable oparations for DNASequence and RNASequence
* **transcribe** — return transcribed sequence (DNA)
* **reverse** — return reversed sequence
* **complement** — return complement sequence
* **reverse_complement** — return reversed-complement sequence

#### Availiable oparations for all the classes:
* slicing by index **seqindex**
* obtaining length of the sequence
* printing the sequence

#### Examples
    my_dna = DNASequence('ataTTgaC')
    my_dna -> Your sequence: ataTTgaC
    my_dna.reverse() -> 'CagTTata'
    my_dna.transcribe() -> 'uauAAcuG'
    my_dna.complement() -> 'tatAActG'
    my_dna.reverse_complement() -> 'GtcAAtat'

### filter_fastq
A Function for filtering reads by specified parameters using [**Biopython**][https://biopython.org/]classes and methods. The function takes 4 arguments as input: input_fastq, gc_bounds, length_bounds, quality_threshold, output_fastq:
* **input_fastq** - a FASTQ-file in the current directory.
* **gc_bounds** - GC % interval for filtering (default is (0, 100). If one numper is in input, it is set as an upper limit.
* **length_bounds** - length interval for filtering, (default is (0, 2**32)). If one numper is in input, it is set as an upper limit.
* **quality_threshold** - average read quality threshold for filtering, default is 0 (phred33 scale).
* **output_fastq** - output file in the current directory containing a  dictionary consisting of fastq sequences.Key is a string, the name of the sequence. Value is a tuple of two strings: sequence and quality.

#### Installation
To run the script you need to clone the repository:

        git clone git@github.com:dashvash/bioinf_modules.git


#### Info
You can get the additional information regarding DNA/RNA operations and FASTQ format below:
* [**Transcription**](https://en.wikipedia.org/wiki/Transcription_(biology))
* [**Translation**](https://en.wikipedia.org/wiki/Translation_(biology))
* [**Complementarity**](https://en.wikipedia.org/wiki/Complementarity_(molecular_biology))
* [**FASTQ**](https://en.wikipedia.org/wiki/FASTQ_format)


#### Contact
This is [Bioinformatics Institute](https://bioinf.me/) study projects by [Daria Vashunina](https://t.me/darivash)
