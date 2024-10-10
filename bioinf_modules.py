""" This is python module that has two functions
run_dna_rna_tools and filter_fastq described below
"""

from typing import Union, Iterable
from add_modules import rna_dna as rd
from add_modules import fastq as fq


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
    operation = args[-1]
    if operation == 'reverse':
        for i in args[:-1]:
            result.append(rd.reverse(i))
    if operation == 'complement':
        for i in args[:-1]:
            result.append(rd.complement(i))
    if operation == 'reverse_complement':
        for i in args[:-1]:
            result.append(rd.reverse_complement(i))
    if operation == 'transcribe':
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
        if (length_bounds[0] <= len(dna) <= length_bounds[1]
            and gb[0] <= fq.count_gc(dna) <= gb[1]
            and fq.quality_threshold(qual) > quality_threshold
            ):
            filter_result[name] = (dna, qual)
    return filter_result
