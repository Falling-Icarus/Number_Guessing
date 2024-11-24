from art import logo
import random

def difficulty():
    choose = input("Chosse a difficulty. Type 'easy' or 'hard': ").lower()
    if choose == "easy":
        return  10
    else:
        return  5

numbers = []

for i in range(1, 101):
    numbers.append(i)

secret_number = random.choice(numbers)

guess = True
while guess == True:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    attempts = difficulty()
    while attempts != 0:
        print(f"You have {attempts} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == secret_number:
            print(f"You got it! The answer was {secret_number}")
            attempts = 0
        elif guess > secret_number:
            print("Too high.\nGuess again.")
            attempts -= 1
        else:
            print("Too low.\nGuess again.")
            attempts -= 1
        if attempts == 0:
            print(f"You've run out of guesses. The number was {secret_number} Start the game again.")
        guess = False