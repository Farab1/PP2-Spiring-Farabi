import re

text = "ab a_aab Aaaaaaaaaaaaab abbbbbb ab abb abbbb abbbbbbb"

x = re.findall (r"\b[A-Z]+[a-z]+\b", text)

print(x)