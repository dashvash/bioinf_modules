# bioinf_modules
A two-function module for working with nucleic acid sequences.

## Description
### run_dna_rna_tools
The function takes any number of arguments with DNA or RNA sequences (str) as input, as well as the name of the operation to be executed as the last argument. After that, it performs the specified action on all the passed sequences and returns the result.

#### Availiable oparations
* **transcribe** — return transcribed sequence
* **reverse** — return reversed sequence
* **complement** — return complement sequence
* **reverse_complement** — return reversed-complement sequence

#### Examples
    run_dna_rna_tools('ATG', 'transcribe') -> 'AUG'
    run_dna_rna_tools('ATG', 'reverse') -> 'GTA'
    run_dna_rna_tools('AtG', 'complement') -> 'TaC'
    run_dna_rna_tools('ATg', 'reverse_complement') -> 'cAT'
    run_dna_rna_tools('ATG', 'aT', 'reverse') -> ['GTA', 'Ta']

### filter_fastq
A Function for filtering reads by specified parameters. The function takes 4 arguments as input: input_fastq, gc_bounds, length_bounds, quality_threshold, output_fastq:
* **input_fastq** - a FASTQ-file in the current directory.
* **gc_bounds** - GC % interval for filtering (default is (0, 100). If one numper is in input, it is set as an upper limit.
* **length_bounds** - length interval for filtering, (default is (0, 2**32)). If one numper is in input, it is set as an upper limit.
* **quality_threshold** - average read quality threshold for filtering, default is 0 (phred33 scale).
* **output_fastq** - output file in the current directory containing a  dictionary consisting of fastq sequences.Key is a string, the name of the sequence. Value is a tuple of two strings: sequence and quality.

#### Examples
For [EXAMPLE_FASTQ](https://github.com/dashvash/bioinf_modules/blob/tools/example_data.py#:~:text=bioinf_modules.py-,example_data,-.py)

        filter_fastq(EXAMPLE_FASTQ, length_bounds=(50, 75)) -> {'@SRX079811': ('AGTTATTTATGCATCATTCTCATGTATGAGCCAACAAGATAGTACAAGTTTTATTGCTATGAGTTCAGTACAACA', 
        '<<<=;@B??@<>@><48876EADEG6B<A@*;398@.=BB<7:>.BB@.?+98204<:<>@?A=@EFEFFFEEFB'), 
        '@SRX079812': ('AGTGAGACACCCCTGAACATTCCTAGTAAGACATCTTTGAATATTACTAGTTAGCCACACTTTAAAATGACCCG',
        '<98;<@@@:@CD@BCCDD=DBBCEBBAAA@9???@BCDBCGF=GEGDFGDBEEEEEFFFF=EDEE=DCD@@BBC')}
#### Installation
To run the script you need to clone the repository:

        git clone git@github.com:dashvash/bioinf_modules.git

#### Info
You can get the additional information regarding DNA/RNA operations and FASTQ format below:
* [**Transcription**](https://en.wikipedia.org/wiki/Transcription_(biology))
* [**Translation**](https://en.wikipedia.org/wiki/Translation_(biology))
* [**Complementarity**](https://en.wikipedia.org/wiki/Complementarity_(molecular_biology))
* [**FASTQ**](https://en.wikipedia.org/wiki/FASTQ_format)

# bio_files_processor
A two-function module for working with text files.

## Description
### convert_multiline_fasta_to_oneline
Takes 2 arguments (input_fasta, output_fasta). Reads the fasta file as input, in which the sequence (DNA/RNA/protein/ …) can be split into several lines, and then saves it to a new fasta file in which each sequence fits into one line.

### parse_blast_output
Takes 2 arguments (input_file, output_file). Function to parse BLAST output to get the best alignment sequence protein. Output is a list of the best protein for each input query.

#### Contact
This is [Bioinformatics Institute](https://bioinf.me/) study projects by [Daria Vashunina](https://t.me/darivash)
