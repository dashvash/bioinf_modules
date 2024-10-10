DNA_COMPLEMENT = {'A': 'T',
                  'a': 't',
                  'C': 'G',
                  'c': 'g',
                  'T': 'A',
                  't': 'a',
                  'G': 'C',
                  'g': 'c'}
RNA_COMPLEMENT = {'A': 'T',
                  'a': 't',
                  'C': 'G',
                  'c': 'g',
                  'U': 'A',
                  'u': 'a',
                  'G': 'C',
                  'g': 'c'}
DNA_TRANSCRIBE = {'A': 'A',
                  'a': 'a',
                  'C': 'C',
                  'c': 'c',
                  'T': 'U',
                  't': 'u',
                  'G': 'G',
                  'g': 'g'}

def is_dna(string: str) -> str:
    dna = {'a', 't', 'c', 'g'}
    return set(string.lower()).issubset(dna)


def is_rna(string: str) -> str:
    rna = {'a', 'u', 'c', 'g'}
    return set(string.lower()).issubset(rna)


def reverse(string: str) -> str:
    if is_dna(string) or is_rna(string):
        return string[::-1]
    else:
        return 'is_not_NA'


def complement(string: str) -> str:
    comp = ''
    if is_dna(string):
        for i in string:
            comp += DNA_COMPLEMENT[i]
    if is_rna(string):
        for i in string:
            comp += RNA_COMPLEMENT[i]
    if is_dna(string) is False and is_rna(string) is False:
        comp = 'is_not_NA'
    return comp


def reverse_complement(string: str) -> str:
    return complement(reverse(string))


def transcribe(string: str) -> str:
    transcript = ''
    if is_dna(string):
        for i in string:
            transcript += DNA_TRANSCRIBE[i]
    if is_rna(string):
        transcript = 'it_is_RNA'
    if is_dna(string) is False and is_rna(string) is False:
        transcript = 'is_not_NA'
    return transcript
