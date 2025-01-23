mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = mydict.get("model")

mydict.update({"year" : 2024})
mydict['color'] = 'red'

print(mydict)
mydict.pop('year')

for x in mydict:
  print('good car')

yourdict = mydict.copy

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)