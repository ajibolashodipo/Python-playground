# finditer
# findall
# match
# search

import re
pattern= '^a|b...s$'
test_string= "blias"
result= re.match(pattern, test_string)
if result:
    print("Search successful")

else:("Search unsuccessful")

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string)
print(result)