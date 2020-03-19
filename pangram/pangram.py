import string

def is_pangram(sentence):
    return not bool(set(string.ascii_lowercase) - set(sentence.lower()))
