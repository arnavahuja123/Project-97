import random

print("Number Guessing Game")

rand = random.randint(1,9)

print("guess a number from 1 to 9")

chances = 0

while chances < 5:
    guess = int(input("enter your guess: "))
    if guess==rand:
        print("Congratulations you won")
        break
    elif guess<rand:
        print("Your guess is too low")
        
    else:
        print("Your guess is too high")
    chances+=1

if not chances < 5:
    print("You Lose!The number is: ", rand)
