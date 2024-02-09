import random
def guess():
    n = random.randint(1, 20)
    print("Hello! What is your name?")
    name = str(input())
    print("Well,", name, ",I am thinking of a number between 1 and 20.")
    i = 0
    while True:
        i = i+1
        g = int(input())
        print("Take a guess")
        if(g < n):
            print("Your guess is too low.")
        if(g>n):
            print("Your guess is too high.")
        if(g == n):
            print("Good job,",name,"! You guessed my number in", i, "guesses!")
            break
guess()