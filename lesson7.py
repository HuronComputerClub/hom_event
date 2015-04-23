#the game
from random import randint

secret = randint(1,100)
guess = 0

def compare(num1, num2):
    if num1 == num2:
        print("Correct")
    elif num1 > num2:
        print("Too high")
    elif num1 < num2:
        print("Too low")
        
while guess != secret:
    guess = int(input("Enter a number:"))
    compare(guess, secret)

print("You guessed the number!")
