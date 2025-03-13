filename = "text2.txt"
text = ("еркелеші ерке қыз")
with open (filename, "w", encoding="utf-8") as file:
    for item in text:
      txt = file.write(item)