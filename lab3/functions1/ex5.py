#ex 5
from itertools import permutations
def perm(string):
    word = permutations(string)
    for i in word:
        print(i)
string = str(input())
perm(string)