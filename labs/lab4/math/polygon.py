import math

side = int(input ('Input number of sides: '))
lenght = int(input ('Input the length of a side: '))

area = (side * pow(lenght,2))/(4* math.tan(math.pi/side))

print('The area of polygon:',area)