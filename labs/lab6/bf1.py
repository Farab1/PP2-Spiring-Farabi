from functools import reduce
list = [3,5,6,9,8,7,3,2]

def multpl(numbers):
    return reduce(lambda x,y: x*y , numbers)
print(multpl(list))