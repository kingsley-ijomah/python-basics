PROTEIN_CODENS = {
    'Methionine': ['AUG'],
    'Phenylalanine': ['UUU','UUC'],
    'Leucine': ['UUA','UUG'],
    'Serine': ['UCU','UCC','UCA','UCG'],
    'Tyrosine': ['UAU','UAC'],
    'Cysteine': ['UGU','UGC'],
    'Tryptophan': ['UGG'],
    'STOP': ['UAA','UAG','UGA']
}

def proteins(strand):
    result = []
    stopped = False
    for codon in codons(strand):
        for key, values in PROTEIN_CODENS.items():
            if codon in values:
                if key == 'STOP':
                    stopped = True

                if stopped == False:
                    result.append(key)

    return result


def codons(strand):
    codons = []

    for i in range(0, len(strand), 3):
        coden_string = "".join(strand[i:i + 3])
        codons.append(coden_string)

    return codons
