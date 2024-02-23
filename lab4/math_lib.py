import math

#ex 1
n = int(input())
print(math.radians(n))

#ex 2
height = int(input())
base_1 = int(input())
base_2 = int(input())
area = 0.5 * (base_1 + base_2) * height
print(area)

#ex 3
n_side = int(input())
l_side = int(input())
area = n_side * (l_side**2) / (4 * math.tan(math.pi / n_side))
print(int(area))

#ex 4
p_base = int(input())
p_height = int(input())
area = p_base * p_height
print(float(area))
