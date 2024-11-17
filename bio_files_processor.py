import os
""" This is python module that has two functions
convert_multiline_fasta_to_oneline and parse_blast_output
"""


def convert_multiline_fasta_to_oneline(input_fasta: str,
                                       output_fasta='output_fasta'):
    """ Function to convert input multiline
    fasta-file to oneline output fasta-file.
    Input is filename in the current directory,
    Output will be created in the same directory with default name output_fasta
    """
    full_path = os.path.abspath(__file__)
    path = os.path.dirname(full_path)

    with open(path + '/' + input_fasta, 'r') as in_fasta:
        with open(path + '/' + output_fasta, 'a') as out_fasta:
            oneline = []
            for line in in_fasta:
                if line.startswith('>'):
                    if len(oneline) > 0:
                        out_fasta.write(''.join(oneline) + '\n')
                        oneline = []
                    out_fasta.write(line)
                else:
                    oneline.append(line.strip())
            if len(oneline) > 0:
                out_fasta.write(''.join(oneline) + '\n')


def parse_blast_output(input_file: str, output_file='parse_output'):
    """ Function to parse BLAST output to get
    the best alignment sequence protein.
    Output is a list of the best protein for each input query.
    """
    full_path = os.path.abspath(__file__)
    path = os.path.dirname(full_path)
    with open(path + '/' + input_file, 'r') as blast_file:
        with open(path + '/' + output_file, 'a') as parse_output:
            parsing = []
            for line in blast_file:
                if line.startswith('Description'):
                    protein = next(blast_file).split('  ')[0]
                    parsing.append(protein)
            sorted_parsing = sorted(parsing)
            for line in sorted_parsing:
                parse_output.write(line + '\n')
