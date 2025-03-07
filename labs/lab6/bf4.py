import math
import time
x=int(input('Your number:'))
y=int(input('miliseconds:'))

print('Analyze...')
time.sleep(y/1000)
mysqrt = math.sqrt(x)

print(f'Square root of {x} after {y} miliseconds is {mysqrt}')