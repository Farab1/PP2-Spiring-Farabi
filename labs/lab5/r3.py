import re

text = "ab a_aab aaaaaaaaaaaaab abbbbbb ab abb abbbb abbbbbbb"

x = re.findall (r"\b[a-z]+_[a-z]+\b", text)

print(x)