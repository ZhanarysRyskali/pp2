#ex 7
n = int(input())
nums = []
for i in range(n):
    x = int(input())
    nums.append(x)
def has33(nums):
    for i in range(len(nums) - 1):
        if (nums[i] == 3 and nums[i+1] == 3):
            return True
    return False
if(has33(nums) == True):
    print("True")
else:
    print("False")