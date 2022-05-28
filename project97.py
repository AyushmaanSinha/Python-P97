import random

number=0
number=random.randint(1,9)
chance=0
print("Guess the number between 1 to 9")


while chance<6:
    guess=int(input("Enter your Guess : "))
    if (guess==number):
        print("Congo! You Won")
        break
    elif (guess<number):
        print("Your guess was lower, try again with a number greater than", guess)
    else:
        print("Your guess is high, try again with a number lesser than", guess)
    chance+=1   

if (not chance<5):
    print("You Lose")
    print("The number is", number)
