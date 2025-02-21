import re

text = "ab aaab aaaaaaaaaaaaab abbbbbb ab abb abbbb abbbbbbb"

x = re.findall(r"\bab{2,3}\b", text)

print(x)
