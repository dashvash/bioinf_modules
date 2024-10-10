def count_gc(seq: str):
    c = seq.count('C')
    g = seq.count('G')
    return (c + g)/len(seq)*100


def quality_threshold(qstring: str):
    total = 0
    for q in qstring:
        total += ord(q)
    return total/len(qstring) - 33
