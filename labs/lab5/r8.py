import re

text = "splitAtUpperCase WeWantToBeSepareted"

x =  re.findall(r'[A-Z]?[a-z]+', text)

print(x)