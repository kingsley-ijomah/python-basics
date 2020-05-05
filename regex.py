# regex examples

# Matching Anything But a Newline e.g ( 123.456.abc.def )
regex_pattern = r"\.(\d{3})|(\w{3})"

# Matching Digits & Non-Digit Characters e.g (06-11-2015)
Regex_Pattern = r"\d[^\d]"

# Matching Whitespace & Non-Whitespace Character ( 12 11 15 )
Regex_Pattern = r"\d{2}\s\d{2}\s\d{2}"

# Matching Word & Non-Word Character ( www.hackerrank.com )
r"\w{3}\W{1}\w{10}\W{1}\w{3}"

# Matching Start & End ( 0qwer. )
Regex_Pattern = r"^\d\w{4}\.$"

# Matching Specific Characters ( 1203x. )  
Regex_Pattern = r'^[1|2|3][1|2|0][x|s|0][3|0|A|a][x|s|u][.|,]$'

# Matching Start & End ( 0qwer. )   
r"^\d\w{4}\.$"

# Excluding Specific Characters ( think? )
Regex_Pattern = r'^[^0-9][^aeiou][^bcDF][^\s][^AEIOU][^.,]$'

# Matching Character Ranges ( h4CkR )
Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z].*'

# Matching One Or More Repetitions ( 1Qa )
Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'

# Matching Ending Items ( Kites )
Regex_Pattern = r'^[a-zA-Z]*e?s'

# Matching Word Boundaries ( Found any match? )
Regex_Pattern = r'\b[aeiouAEIOU][a-z]*\b'

# Capturing & Non-Capturing Groups ( okokok! cya )
Regex_Pattern = r'(ok){3}'

# Matching {x, y} Repetitions ( 3threeormorealphabets. )
Regex_Pattern = r'^\d{1,2}[a-zA-Z]{3,}\.{0,3}$'