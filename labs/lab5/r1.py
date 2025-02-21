import re

text = "ab aaab aaaaaaaaaaaaab abbbbbb ab abb abbbb abbbbbbb"

x = re.match(r"a+b", text)

print(x)