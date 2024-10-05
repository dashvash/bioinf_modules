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



