import os


def convert_multiline_fasta_to_oneline(input_fasta: str,
                                       output_fasta='output_fasta'):
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
