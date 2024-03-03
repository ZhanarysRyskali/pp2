import os


#1
path = input()
print("Directories:")
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
        print(i)
print("\nFiles")
for i in os.listdir(f"{path}"):
    print(i)
print("\nAll Directories and Files:")
for root, directories, files in os.walk(path):
    print(f"\nDirectory: {root}")
    print("Directories:")
    for directory in directories:
        print(os.path.join(root, directory))

#2
path = input()
if(os.path.exists(f"{path}")):
    if(os.access(path, os.R_OK)):
        print("It is readable")
    else:
        print("It is not readable")
    if(os.access(path, os.W_OK)):
        print("It is writable")
    else:
        print("It is not writable")
    if(os.access(path, os.X_OK)):
        print("It is executable")
    else:
        print("It is not executable")
else:
    print("Path doesn't exist")

#3
path = input()
if(os.path.exists(f"{path}")):
    print(os.path.basename(path))
    print(os.path.dirname(path))
else:
    print("Path doesn't exist")

#4
path = input()
with open(path, 'r') as file:
    s = 0
    for line in file:
        s += 1
    print(s)

#5
list = []
for i in range(3):
    list.append(input())
with open("words.txt", 'w') as file:
    file.write(str(list))

#6
letter = ord('A')-1
for i in range(26):
    letter = letter + 1
    filename = str(chr(letter)) + ".txt"
    with open(filename, 'w') as file:
        file.write(str(letter))

#7
with open("Copy.txt", 'w') as file:
    file.write("Content")
with open("Copy.txt", 'r') as file:
    data = file.read()
with open("Paste.txt", 'a') as file:
    file.write(data)

#8
path = input()
if(os.path.exists(f"{path}") and os.access(f"{path}", os.W_OK)):
    os.remove(path)
else:
    print("Path doesn't exist or you have no access")
