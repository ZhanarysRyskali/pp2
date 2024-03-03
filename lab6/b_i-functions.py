import math
import time

#1
list = [1, 2, 3, 4, 5]
print(math.prod(list))


#2
string = input()
l = 0
b = 0
for i in string:
    if i.islower():
        l+=1
    if i.isupper():
        b+=1
print(f"lower letter:{l}")
print(f"upper letters:{b}")


#3
string = input()
if string == string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


#4
number = int(input())
milis = int(input())
time.sleep(milis/1000)
print(math.sqrt(number))

#5
tupe1 = (5, "Hello", 0)
tupe2 = (True, "string", 9)
print(all(tupe1))
print(all(tupe2))