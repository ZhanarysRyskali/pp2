# ex 3
heads = int(input())
legs = int(input())
def solve(heads, legs):
    y = (legs/2)-heads
    x = 2*heads - legs/2
    print("Rabbits:", int(y))
    print("Chickens:", int(x))
solve(heads, legs)