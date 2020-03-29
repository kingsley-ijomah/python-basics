def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands length not equal')
        
    return len([[x,y] for x,y in zip(strand_a,strand_b) if x != y])
