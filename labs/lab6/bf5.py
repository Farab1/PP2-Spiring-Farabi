import ast

user_input = input("Input tuple elements with comma:")

my = tuple(map(ast.literal_eval, user_input.split(',')))

if all(my):
    print('All elements in the tuple are true')
else:
    print('We have false elements in tuple')
