import random

def guess_the_number(start, end):
    number = random.randint(start, end)
    tries = 1
    print("\nOkay. I'm thinking of a number between %i and %i." % (start, end))
    while True:
        print("Take a guess.")  
        guess = int(input())
        if guess == number:
            print("\nCongrats! I was thinking of " + str(number) + "!")
            print("It only took you %i tries!" % tries)
            break
        elif guess > number:
            print("You guessed too high. Try lower.")
            tries = tries + 1
        else:
            print("You guessed too low. Try higher.")
            tries = tries + 1

print("What's the low point number?")
low_point = int(input())
print("What's the high point number?")
high_point = int(input())

guess_the_number(low_point, high_point)
