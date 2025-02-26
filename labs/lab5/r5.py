import re

text = "ab a_aab aaaaaaaaaaaaab abbbbbb ab abb abbbb abbbbbbb"

x = re.findall (r'a.*b' , text)

print(x)