mytuple = ('apple','banana','waatermelon')
y = list(mytuple)
y[2]='melon'
y.append("orange")
mytuple = tuple(y)

(green,afric,yellow,orange) = mytuple
print(green,afric,yellow,orange)

for x in mytuple:
    print('fruits')

yourtuple = ('sugar','water','bread')

ourtuple = mytuple+yourtuple
print('total:', ourtuple)