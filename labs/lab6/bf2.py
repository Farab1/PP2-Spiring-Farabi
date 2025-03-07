import re 
txt = "Satymkul Farabi Medethanuly"
u=len(re.findall(r"[A-Z]",txt))
l=len(re.findall(r"[a-z]",txt))

print('Uppercase letters:',u)
print('Lowercase letters:',l)