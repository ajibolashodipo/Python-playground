import re
import os

os.chdir(r'C:\Users\AjibolaShodipo\PycharmProjects\PythonFromScratch\Somewhat_Advanced\regex')

# raw string: interprets a string literally


text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
cat
mat
pat
bat
'''

sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'[89]00[-.*]\d\d\d[-.*]\d\d\d\d')
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z][a-z]*')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)



# with open("data.txt", "r") as f:
#     contents = f.read()
#
#     matches = pattern.finditer(contents)
#
#     for match in matches:
#         print(match)
