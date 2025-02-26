import re

text = "ab a_aab aaaaaaaaaaaaab abbbbbb ab abb abbbb abbbbbbb"

x = re.sub(r'[ ,.]',':', text)

print(x)