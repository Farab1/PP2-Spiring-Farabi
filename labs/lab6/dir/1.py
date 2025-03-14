import os
'''"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists'''

def list_d(path):
    try:
        items = os.listdir(path)
        only_dir = [item for item in items if os.path.isdir(os.path.join(path,item))]
        only_file = [item for item in items if os.path.isfile(os.path.join(path,item))]
        print("Folders")
        print(only_dir)
        print("\n Files")
        print(only_file)
        print("\n All ")
        print(items)
        
    except FileNotFoundError:
        print("Error, there are no such file")
    except PermissionError:
        print("Error, you dont have a permission to file")
path = input("Enter a path to file: ")

list_d(path)