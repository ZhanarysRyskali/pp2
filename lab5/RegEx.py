import re
#ex 1
match = input("matches a string that has an 'a' followed by zero or more 'b''s:")
if re.search(r"^ab*$", match):
    print("Valid")
else:
    print("Not valid")

#ex 2
match = input("program that matches a string that has an 'a' followed by two to three 'b':")
if re.search(r"^ab{2,3}", match):
    print("Valid")
else:
    print("Not valid")

#ex 3
match = input("find sequences of lowercase letters joined with a underscore:")
if re.search(r"[a-b]+_[a-b]+", match):
    print("Valid")
else:
    print("Not valid")

#ex 4
match = input("find the sequences of one upper case letter followed by lower case letters:")
if re.search(r"^[A-B]{1}[a-b]+$", match):
    print("Valid")
else:
    print("Not valid")

#ex 5
match = input("that matches a string that has an 'a' followed by anything, ending in 'b':")
if re.search(r"^a.+b$", match):
    print("Valid")
else:
    print("Not valid")

#ex 6
match = input("to replace all occurrences of space, comma, or dot with a colon:")
result = re.sub(r"( |,|\.)", ":", match)
print(result)

#ex 7
def upper(a):
    return a.group(0).upper()[1::]
match = input("convert snake case string to camel case string:")
print(re.sub("_[a-z]",upper,match))

#ex 8
match = input("program to split a string at uppercase letters:")
result = re.split(r"(?=[A-Z])", match)
print(result)

#ex 9
match = input("insert spaces between words starting with capital letters:")
result = re.sub(r"(?=[A-Z])", " ", match)
print(result)

#ex 10
match = input("convert a given camel case string to snake case:")
result = re.sub(r"([A-Z])", r"_\1", match).lower()
print(result)
