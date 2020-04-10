SCORES = [
    (1, 'A, E, I, O, U, L, N, R, S, T'),
    (2, 'D, G'),
    (3, 'B, C, M, P'),
    (4, 'F, H, V, W, Y'),
    (5, 'K'),
    (8, 'J, X'),
    (10, 'Q, Z')
]
def score(word):
    return sum([letter_scores(letter) for letter in word.upper()])

def letter_scores(letter):
    return sum([score for score,values in SCORES if letter in values])
