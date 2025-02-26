import re

text = "splitAtUpperCase WeWantToBeSepareted"

x = x = re.findall(r'[A-Z]?[a-z]+', text)

print(x)