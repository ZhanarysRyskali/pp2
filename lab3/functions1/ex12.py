num = []
for i in range(3):
    x = int(input())
    num.append(x)
def histogram(num):
    for i in num:
        print('*' * i)
histogram(num)