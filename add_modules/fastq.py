def gc_func(string: str):
    C = string.count('C')
    G = string.count('G')
    return (C + G)/len(string)*100


def quality_threshold_func(qstring: str):
    total = 0
    for i in qstring:
        total += ord(i)
    return total/len(qstring)
