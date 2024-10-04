from add_modules import rna_dna as rd
from add_modules import fastq as fq

def run_dna_rna_tools(*args):
    result = []
    if args[-1] == 'reverse':
        for i in args[:-1]:
            result.append(rd.reverse(i))
    if args[-1] == 'complement':
        for i in args[:-1]:
            result.append(rd.complement(i))
    if args[-1] == 'reverse_complement':
        for i in args[:-1]:
            result.append(rd.reverse_complement(i))
    if args[-1] == 'transcribe':
        for i in args[:-1]:
            result.append(rd.transcribe(i))
    if len(result) == 1:
        return result[0]
    else:
        return result
    

def filter_fastq(seqs, gc_bounds=(0, 100),
                 length_bounds=(0, 2**32),
                 quality_threshold=0):
    if isinstance(gc_bounds, (int, float)):
        gc_bounds = (0, gc_bounds)
    if isinstance(length_bounds, (int, float)):
        length_bounds = (0, length_bounds)
    filter_result = {}
    for name in seqs:
        dna = seqs[name][0]
        qual = seqs[name][1]
        if len(dna) >= length_bounds[0] and len(dna) <= length_bounds[1]:
            if fq.gc_func(dna) >= gc_bounds[0] and fq.gc_func(dna) <= gc_bounds[1]:
                if fq.quality_threshold_func(qual) > quality_threshold + 33:
                    filter_result[name] = (dna, qual)
    return filter_result    