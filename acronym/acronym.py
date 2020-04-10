import re

def abbreviate(words):
    return ''.join(re.findall(r"(?<![A-Z'])[A-Z]", words.upper()))
