import os
import pytest
from fastq_filtrator import filter_fastq
from Bio import SeqIO

@pytest.fixture
def input_fastq():
    file_path = 'example.fastq'
    assert os.path.exists(file_path), f"file {file_path} does not exist"
    return file_path

def test_output_file_exist(input_fastq):
    target = 'filtered_file'
    filter_fastq(input_fastq, length_bounds=[20, 100])
    output_file_path = os.path.join('filtered', target)
    assert os.path.exists(output_file_path), f"file {output_file_path} does not exist"

def test_output_file_isnt_empty(input_fastq):
    target = 'filtered_file'
    filter_fastq(input_fastq, length_bounds=[20, 100])
    output_file_path = os.path.join('filtered', target)
    assert os.path.getsize(output_file_path) > 0

def test_bad_quality_threshold():
    with pytest.raises(TypeError):
        filter_fastq("example.fastq", quality_threshold="high")

def test_bad_quality_threshold2():
    with pytest.raises(TypeError):
        filter_fastq("example.fastq", quality_threshold="1000")

def test_bad_gc_bounds():
    with pytest.raises(TypeError):
        filter_fastq("example.fastq", gc_bounds="high")

def test_bad_gc_bounds2():
    with pytest.raises(TypeError):
        filter_fastq("example.fastq", gc_bounds="100000")

def test_result1():
    target = 2

    output_file = os.path.join('filtered', 'filtered_file')
    if os.path.exists(output_file):
        os.remove(output_file)

    input_fastq = "example.fastq"
    filter_fastq(input_fastq, length_bounds=[50, 75])

    reads = list(SeqIO.parse(output_file, "fastq"))
    assert len(reads) == target

def test_result2():
    target = 5

    output_file = os.path.join('filtered', 'filtered_file')
    if os.path.exists(output_file):
        os.remove(output_file)

    input_fastq = "example.fastq"
    filter_fastq(input_fastq, gc_bounds=[10, 40])

    reads = list(SeqIO.parse(output_file, "fastq"))
    assert len(reads) == target


