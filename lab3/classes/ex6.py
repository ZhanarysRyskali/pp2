def prime(el):
    if(el<2):
        return False
    for i in range(2, int(el**0.5) + 1):
        if(el % i == 0):
            return False
    return True
def filtering(nums):
    return list(filter(lambda x: prime(x), nums))
n = int(input())
nums = []
for i in range(n):
    x = int(input())
    nums.append(x)
print(filtering(nums))