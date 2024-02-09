#ex 6
str = str(input())
s = str.split()[::-1]
l = []
for i in s:
    l.append(i)
for words in l:
    print(words, end = " ")