def count_gc(seq: str):
    c = seq.count('C')
    g = seq.count('G')
    return (c + g)/len(seq)*100


def quality_threshold(qstring: str):
    total = 0
    for q in qstring:
        total += ord(q)
    return total/len(qstring) - 33


def read_fastq(file_path):
    with open(file_path, 'r') as file:
        seqs = {}
        lines = file.readlines()
        for num in range(0,len(lines),4):
            seqs[lines[num].rstrip()] = (lines[num+1].rstrip(),lines[num+3].rstrip())
    return seqs