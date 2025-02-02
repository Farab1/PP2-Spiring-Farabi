from itertools import permutations

def permut(my_input : str):
    for x in set(permutations(my_input)):
        print(''.join(perm))
        
my=input()
permut(my)