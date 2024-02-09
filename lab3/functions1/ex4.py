#ex 4
n = int(input())
list = []
for i in range(n):
    el = int(input())
    list.append(el)
def prime(el):
    if(el<2):
        return False
    for i in range(2, int(el**0.5) + 1):
        if(el % i == 0):
            return False
    return True
for el in list:
    if(prime(el) == True):
        print(el, "is Prime")
    else:
        print(el, "is not Prime")