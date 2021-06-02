import re
#
# string = "search inside of this test this please"
#
# patt = "this"
# a = re.findall(patt, string)
# print(a)

# pattern= re.compile('this')


# password checker
# password must contain at least seven characters and end with a number
pattern = r"[a-zA-Z0-9$%#@]{7,}[0-9]"
password = "ahsfjr5"
res = re.match(pattern, password)
if res:
    print("Search successful huhu")
else:
    print("Search unsuccessful")
