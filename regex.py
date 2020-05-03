# regex examples

# Matching Anything But a Newline e.g ( 123.456.abc.def )
regex_pattern = r"\.(\d{3})|(\w{3})"

# Matching Digits & Non-Digit Characters e.g (06-11-2015)
Regex_Pattern = r"\d[^\d]"

# Matching Whitespace & Non-Whitespace Character ( 12 11 15 )
Regex_Pattern = r"\d{2}\s\d{2}\s\d{2}"