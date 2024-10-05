# bioinf_modules
A two-function module for working with nucleic acid sequences.

## Description
### run_dna_rna_tools
The function takes any number of arguments with DNA or RNA sequences (str) as input, as well as the name of the operation to be executed as the last argument. After that, it performs the specified action on all the passed sequences and returns the result.

#### Availiable oparetions
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
A Function for filtering reads by specified parameters. The function takes 4 arguments as input: seqs, gc_bounds, length_bounds, quality_threshold:
* **seqs** - a dictionary consisting of fastq sequences.Key is a string, the name of the sequence. Value is a tuple of two strings: sequence and quality.
* **gc_bounds** - GC % interval for filtering (default is (0, 100). If one numper is in input, it is set as an upper limit.
* **length_bounds** - length interval for filtering, (default is (0, 2**32)). If one numper is in input, it is set as an upper limit.
* **quality_threshold** - average read quality threshold for filtering, default is 0 (phred33 scale).

#### Examples
For EXAMPLE_FASTQ from example_data.py:

        filter_fastq(EXAMPLE_FASTQ, length_bounds=(50, 75)) -> {'@SRX079811': ('AGTTATTTATGCATCATTCTCATGTATGAGCCAACAAGATAGTACAAGTTTTATTGCTATGAGTTCAGTACAACA', 
        '<<<=;@B??@<>@><48876EADEG6B<A@*;398@.=BB<7:>.BB@.?+98204<:<>@?A=@EFEFFFEEFB'), 
        '@SRX079812': ('AGTGAGACACCCCTGAACATTCCTAGTAAGACATCTTTGAATATTACTAGTTAGCCACACTTTAAAATGACCCG',
        '<98;<@@@:@CD@BCCDD=DBBCEBBAAA@9???@BCDBCGF=GEGDFGDBEEEEEFFFF=EDEE=DCD@@BBC')}
