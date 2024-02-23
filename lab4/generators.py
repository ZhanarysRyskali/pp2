#ex 1
def square():
    N = int(input())
    for i in range(1, N+1):
        yield i**2
a = square()
print(list(a))

#ex 2
def even():
    n = int(input())
    for i in range(0, n+1, 2):
        yield i
b = even()
print(list(b))

#ex 3
def divisible():
    n = int(input())
    for i in range(0, n+1):
        if(i%3 == 0 and i%4 == 0):
            yield i
c = divisible()
print(list(c))

#ex 4
def squares():
    x = int(input())
    y = int(input())
    for i in range(x, y+1):
        yield i**2
d = squares()
print(list(d))

#ex 5
def decreasing():
    n = int(input())
    for i in range(n, -1, -1):
        yield i
e = decreasing()
print(list(e))