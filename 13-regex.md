# automate boring stuff with python pdf

https://pythex.org/
https://regex101.com/
https://www.hackerrank.com/domains/regex
http://www.restore.ac.uk/geo-refer/38330mtuks00y19740000.php
---------------------

Review of Regex Symbols Meaning
-------------------------------

. ^ $ * + ? {n} {n,m}? \ [] () | \d \w \s \D \W \S \A \b \B \Z 

. matches any character, except newline characters.
^spam means the string must begin with spam.
$ Matches the end of the string
* matches zero or more of the preceding group.
+ matches one or more of the preceding group.
? matches zero or one of the preceding group.
{n} matches exactly n of the preceding group.
{n,} matches n or more of the preceding group.
{,m} matches 0 to m of the preceding group.
{n,m} matches at least n and at most m of the preceding group.
{n,m}? or *? or +? performs a non-greedy match of the preceding group.
\ Either escapes special characters or signals a special sequence
[abc] matches any character between the brackets (such as a, b, or c).
[^abc] matches any character that isn’t between the brackets.
(?:aiLmsux) matches the characters aiLmsux literally (case sensitive)
(?=...) called 'lookahead' Isaac (?=Asimov) will match 'Isaac ' only if it’s followed by 'Asimov'.
(?!...) called negative lookahead. Isaac (?!Asimov) match 'Isaac ' if not followed by 'Asimov'.
(?<=...) called a positive lookbehind assertion. (?<=abc)def will find a match in 'abcdef'
(?<!...) called negative lookbehind (?!abc)def will match 'def' in 123def because 123 is not abc
| A|B, creates a regular expression that will match either A or B
\d, \w, and \s match a digit, word, or space character, respectively.
\D, \W, and \S match anything except a digit, word, or space character,respectively.
\b Matches the empty string, but only at the beginning or end of a word
\B Matches the empty string, but only when it is not at the beginning or end of a word
\Z Matches only at the end of the string.
-

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
>>> Phone number found: 415-555-4242

grouping
--------
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1)
>>> '415'
mo.group(2)
>>> '555-4242'
mo.group(0)
>>> '415-555-4242'
mo.group()
>>> '415-555-4242

mo.groups()
>>> ('415', '555-4242')
areaCode, mainNumber = mo.groups()
print(areaCode)
>>> 415
print(mainNumber)
>>> 555-4242

match parentheses with escape
-----------------------------
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
mo.group(1)
>>> '(415)'
mo.group(2)
>>> '555-4242'


pipe acts like an or
--------------------
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
mo1.group()
>>> 'Batman'
mo2 = heroRegex.search('Tina Fey and Batman')
mo2.group()
>>> 'Tina Fey'

match multiple with pipe & parentheses
--------------------------------------
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
>>> 'Batmobile'
mo.group(1)
>>> 'mobile'

matching with question mark for optinoal
matches area code and no area code
----------------------------------------
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
mo1.group()
>>> '415-555-4242'
mo2 = phoneRegex.search('My number is 555-4242')
mo2.group()
>>> '555-4242'

match zero or more with the star (*)
------------------------------------
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batwowowowoman')
mo.group()
>>> 'Batwowowowoman'

match one or more with the plus (+)
-----------------------------------
>>> batRegex = re.compile(r'Bat(wo)+man')
>>> mo1 = batRegex.search('The Adventures of Batwoman')
>>> mo1.group()
'Batwoman'

>>> mo2 = batRegex.search('The Adventures of Batwowowowoman')
>>> mo2.group()
'Batwowowowoman'

>>> mo3 = batRegex.search('The Adventures of Batman')
>>> mo3 == None
True

Matching Specific Repetitions with Braces
-----------------------------------------
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group()
>>> 'HaHaHa'

mo2 = haRegex.search('Ha')
mo2
>>> True

Greedy and Non-greedy Matching
------------------------------
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()
>>> 'HaHaHaHaHa'

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()
>>> 'HaHaHa'

The findall() vs search()
-------------------------
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo.group()
>>> '415-555-9999'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
>>> ['415-555-9999', '212-555-0000']

Character Classes
-----------------
\d  Any numeric digit from 0 to 9.
\D  Any character that is not a numeric digit from 0 to 9.
\w  Any letter, numeric digit, or the underscore character. (matching “word” characters)
\W  Any character that is not a letter, numeric digit, or the underscore character.
\s  Any space, tab, or newline character. (Think of this as matching “space” characters.)
\S  Any character that is not a space, tab, or newline.

xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids)
>>> ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids']

Making Your Own Character Classes[]
-----------------------------------
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('RoboCop eats')
>>> ['o', 'o', 'o', 'e', 'a']


negative character class (^)
caret within [] is diff to care outside 
---------------------------------------
consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('RoboCop eats')
>>> ['R', 'b', 'C', 'p', ' ', 't', 's']

The Caret at start of regex (^)
match most occur at the beginning 
---------------------------------
beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello, world!')
>>> <re.Match object; span=(0, 5), match='Hello'>
beginsWithHello.search('He said hello.') == None
>>> True


Dollar Sign Characters ($)
match occurs at the end
--------------------------
endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
>>> <re.Match object; span=(16, 17), match='2'>
endsWithNumber.search('Your number is forty two.') == None
>>> True

 r'^\d+$' start and end as digits
 --------------------------------
wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')
 >>> <re.Match object; span=(0, 10), match='1234567890'>
wholeStringIsNum.search('12345xyz67890') == None
 >>> True
wholeStringIsNum.search('12 34567890') == None
 >>> True

The Wildcard Character (.)
--------------------------
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')
>>> ['cat', 'hat', 'sat', 'lat', 'mat']

Matching Everything with Dot-Star (.*)
match any character except for a newline.
-----------------------------------------
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
mo.group(1)
>>> 'Al'
mo.group(2)
>>> 'Sweigart'
-

The dot-star uses greedy mode use (.*?) for non greedy
------------------------------------------------------
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
mo.group()
>>> '<To serve man>'

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
mo.group()
>>> '<To serve man> for dinner.>'
-

Substituting Strings with the sub() Method
------------------------------------------
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
>>> 'CENSORED gave the secret documents to CENSORED.'

Managing Complex Regexes
------------------------
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}
(\s*(ext|x|ext.)\s*\d{2,5})?)')

above can be transformed to below
---------------------------------
phoneRegex = re.compile(r'''(
 (\d{3}|\(\d{3}\))?             # area code
 (\s|-|\.)?                     # separator
 \d{3}                          # first 3 digits
 (\s|-|\.)                      # separator
 \d{4}                          # last 4 digits
 (\s*(ext|x|ext.)\s*\d{2,5})?   # extension
 )''', re.VERBOSE)