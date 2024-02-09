#ex 10
n = int(input())
a = []
for i in range(n):
    x = int(input())
    a.append(x)
a.sort()
for i in range(n - 1):
    if(a[i] != a[i+1]):
        print(a[i], end = " ")