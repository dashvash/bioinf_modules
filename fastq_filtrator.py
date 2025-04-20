import os
import argparse
import logging
from abc import ABC, abstractmethod
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import gc_fraction

class BiologicalSequence(ABC):
    def __init__(self, seq: str):
        self.seq = seq
        self.length = len(self.seq)
        if not self.is_bioseq():
            raise ValueError("This is not biosequence")
        
    def seqindex(self, index):
        return self.seq[index]
    
    def __repr__(self):
        return f"Your sequence: {self.seq}"
    
    @abstractmethod
    def is_bioseq(self):
        pass


class NucleicAcidSequence(BiologicalSequence):
    def is_bioseq(self):
        alphabet = {'a', 'u', 'c', 'g', 't'}
        return set(self.seq.lower()).issubset(alphabet)
    
    COMPLEMENT = {'A': 'T', 'a': 't',
                  'C': 'G', 'c': 'g',
                  'T': 'A', 't': 'a',
                  'G': 'C', 'g': 'c',
                  'U': 'A', 'u': 'a'}
          
    def complement(self):    
        return ''.join(self.COMPLEMENT[i] for i in self.seq)

    def reverse(self):
        return self.seq[::-1]

    def reverse_complement(self):
        return ''.join(self.COMPLEMENT[i] for i in self.seq[::-1])


class DNASequence(NucleicAcidSequence):
    def transcribe(self):
        DNAtoRNA = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C', 'a': 'u', 't': 'a', 'c': 'g', 'g': 'c'}
        return ''.join(DNAtoRNA[i] for i in self.seq)


class RNASequence(NucleicAcidSequence):
    pass

class AminoAcidSequence(BiologicalSequence):
    def is_bioseq(self):
        alphabet = {'g', 'a', 'v', 'l', 'i',
                    'c', 'm', 's', 't', 'f',
                    'y', 'w', 'd', 'e', 'n',
                    'q', 'h', 'k', 'r', 'p'}
        return set(self.seq.lower()).issubset(alphabet)
    

parser = argparse.ArgumentParser(prog ='FASTQ-filtrator', description="Filtration parameters", epilog='Have a good day!')
parser.add_argument("input_fastq", help="Path to the FASTQ file")
parser.add_argument("--gc_bounds", type=float, nargs='*', default=[0, 100],
                        help="Interval for GC %% value (one value = max only, two = min and max)")
parser.add_argument("--length_bounds", type=float, nargs='*', default=[0, 2**32],
                        help="Interval for length value (one value = max only, two = min and max)")
parser.add_argument("--quality_threshold", type=float, default=0,
                        help="Average read quality threshold for filtering")


logging.basicConfig(
    filename='filter_fastq.log',
    filemode='a',
    format='%(asctime)s [%(levelname)s] %(message)s',
    level=logging.INFO
)

def filter_fastq(input_fastq, gc_bounds=(0, 100),
                 length_bounds=(0, 2**32),
                 quality_threshold=0, output_fastq='filtered_file'):
    """ Function to filter sequences by the given parameter's values
    Args:
        input_fastq: path to a fastq-file to be filtered
        gc_bounds(tuple/int/float): interval for GC % value
        or the upper limit if int/float
        length_bounds(tuple/int/float): interval for length value
        or the upper limit if int/float
        quality_threshold(int, float): average read
        quality threshold for filtering
        output_fastq: name for the output file
        created in /filtered/. Default name is filtered_file.
    """
    
    try:

        logging.info(f"Starting filtering for {input_fastq} with GC bounds {gc_bounds}, "
                     f"length bounds {length_bounds}, quality threshold {quality_threshold}")
        
        if len(length_bounds) == 1:
            length_bounds = [0, length_bounds[0]]
        if len(gc_bounds) == 1:
            gc_bounds = [0, length_bounds[0]]

        full_path = os.path.abspath(__file__)
        path = os.path.dirname(full_path)
        os.makedirs(os.path.join(path, 'filtered'), exist_ok=True)
        output_path = os.path.join(path, 'filtered', output_fastq + '.fastq')

        with open(os.path.join(path, 'filtered', output_fastq), "a") as output_file:
            filter_result = []
            for rec in SeqIO.parse(input_fastq, "fastq"):
                length = len(rec.seq)
                mean_qual = sum(rec.letter_annotations["phred_quality"]) / len(rec.letter_annotations["phred_quality"])
                gc_content = gc_fraction(rec.seq) * 100

                if (length_bounds[0] <= length <= length_bounds[1]
                        and mean_qual > quality_threshold
                        and gc_bounds[0] <= gc_content <= gc_bounds[1]):
                    filter_result.append(SeqRecord(rec.seq,
                                                   id=rec.id,
                                                   letter_annotations=rec.letter_annotations))
            SeqIO.write(filter_result, output_file, "fastq")

            logging.info(f"Filtered {len(filter_result)} reads saved to {output_file.name}")
            print(f"Filtered {len(filter_result)} reads saved to {output_file.name}")

    except Exception as e:
        logging.error(f"Error while filtering FASTQ: {e}")
        print(f"Error: {e}")
        raise

if __name__ == '__main__':
    args = parser.parse_args()
    filter_fastq(args.input_fastq, gc_bounds=args.gc_bounds, 
                 length_bounds=args.length_bounds, quality_threshold=args.quality_threshold)
