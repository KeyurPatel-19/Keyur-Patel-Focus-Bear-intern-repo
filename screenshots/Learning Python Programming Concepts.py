# Hello, Python!

print("Hello, Keyur!")
print("Have fun coding and building amazing things!")

# Simple Math

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)

# Your Age in Dog Years

age = int(input("Enter your age: "))
dog_years = age * 7

print("Your age in dog years is:", dog_years)

# Favourite Food

food = input("What is your favourite food? ")

print("Wow! " + food + " sounds delicious! I also like that food.")

# Number Guessing Game

import random

number = random.randint(1, 10)

while True:
    user_input = input("Guess a number between 1 and 10 (or type 'q' to quit): ")
    
    if user_input.lower() == 'q':
        print("You quit the game. The number was:", number)
        break

    guess = int(user_input)

    if guess == number:
        print("Correct! You guessed it right!")
        break
    else:
        print("Wrong guess! Try again.")
