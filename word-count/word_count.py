import re

def count_words(sentence):
    words = re.findall(r"[a-z\d]+'?[a-z\d]*(?<!')", sentence.lower())

    return dict([(x, words.count(x)) for x in words])
