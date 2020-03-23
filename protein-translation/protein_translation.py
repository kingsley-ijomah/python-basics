PROTEIN_CODENS = {
    'Methionine' : ['AUG'],
    'Phenylalanine' : ['UUU', 'UUC'],
    'Leucine' : ['UUA', 'UUG'],
    'Serine' : ['UCU', 'UCC', 'UCA', 'UCG'],
    'Tyrosine' : ['UAU', 'UAC'],
    'Cysteine' : ['UGU', 'UGC'],
    'Tryptophan' : ['UGG'],
    'STOP' : ['UAA', 'UAG', 'UGA']
}
def proteins(strand):
    proteins = []
    stopped = False

    for i in range(0, len(strand), 3):
        codon = strand[i:i + 3]
        for key, values in PROTEIN_CODENS.items():
            if codon in values:
                if key == 'STOP':
                    stopped = True
                if not stopped:
                    proteins.append(key)

    return proteins
