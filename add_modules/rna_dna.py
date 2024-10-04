def is_dna(string: str):
    dna = {'a', 't', 'c', 'g'}
    return set(string.lower()).issubset(dna)


def is_rna(string: str):
    rna = {'a', 'u', 'c', 'g'}
    return set(string.lower()).issubset(rna)

dna_complement = {'A': 'T',
                  'a': 't',
                  'C': 'G',
                  'c': 'g',
                  'T': 'A',
                  't': 'a',
                  'G': 'C',
                  'g': 'c'}
rna_complement = {'A': 'T',
                  'a': 't',
                  'C': 'G',
                  'c': 'g',
                  'U': 'A',
                  'u': 'a',
                  'G': 'C',
                  'g': 'c'}
dna_transcribe = {'A': 'A',
                  'a': 'a',
                  'C': 'C',
                  'c': 'c',
                  'T': 'U',
                  't': 'u',
                  'G': 'G',
                  'g': 'g'}


def reverse(string: str):
    if is_dna(string) or is_rna(string):
        return string[::-1]
    else:
        return 'is_not_NA'


def complement(string: str):
    comp = ''
    if is_dna(string):
        for i in string:
            comp += dna_complement[i]
    if is_rna(string):
        for i in string:
            comp += rna_complement[i]
    if is_dna(string) is False and is_rna(string) is False:
        comp = 'is_not_NA'
    return comp


def reverse_complement(string: str):
    return complement(reverse(string))


def transcribe(string: str):
    transcript = ''
    if is_dna(string):
        for i in string:
            transcript += dna_transcribe[i]
    if is_rna(string):
        transcript = 'it_is_RNA'
    if is_dna(string) is False and is_rna(string) is False:
        transcript = 'is_not_NA'
    return transcript
