""" This is python module that has two functions
run_dna_rna_tools and filter_fastq described below
"""

from add_modules import rna_dna as rd
from add_modules import fastq as fq
from typing import Union, Iterable


def run_dna_rna_tools(*args: Iterable[str]) -> Union[str, list[str]]:
    """ Function to apply diffrent operations to DNA/RNA string
    Args:
        *args: variable length arguments (str) - DNA/RNA sequences
        and operation's name
    Returns:
        if there is only one DNA/RNA string:
            str: DNA/RNA string after the applied operation
        if there are several DNA/RNA strings:
            list: a list containing DNA/RNA (str) after the applied operation
    """
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


def filter_fastq(seqs: dict, gc_bounds=(0, 100),
                 length_bounds=(0, 2**32),
                 quality_threshold=0) -> dict:
    """ Function to filter sequences by the given parameter's values
    Args:
        seqs (dict): dictionary containing sequences
        names as keys and sets as values.
        Set contains sequence(str) and quality(str).
        gc_bounds(tuple/int/float): interval for GC % value
        or the upper limit if int/float
        length_bounds(tuple/int/float): interval for length value
        or the upper limit if int/float
        quality_threshold(int, float): average read
        quality threshold for filtering
    """
    if isinstance(gc_bounds, (int, float)):
        gc_bounds = (0, gc_bounds)
    if isinstance(length_bounds, (int, float)):
        length_bounds = (0, length_bounds)
    filter_result = {}
    for name in seqs:
        dna = seqs[name][0]
        qual = seqs[name][1]
        gb = gc_bounds
        if len(dna) >= length_bounds[0] and len(dna) <= length_bounds[1]:
            if fq.gc_func(dna) >= gb[0] and fq.gc_func(dna) <= gb[1]:
                if fq.quality_threshold_func(qual) > quality_threshold + 33:
                    filter_result[name] = (dna, qual)
    return filter_result
