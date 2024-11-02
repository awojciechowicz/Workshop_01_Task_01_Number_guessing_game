from random import randint

def let_me_guess():
    while True:
        guess = input("Guess the number: ")
        try:
            guess = float(guess)
            return guess
        except ValueError:
            print("It's not a number")

def check_the_value(number, guess):
    if guess < number:
        # print("Too small!")
        return "Too small!"
    elif guess > number:
        # print("Too big!")
        return "Too big!"
    elif guess == number:
        # print("You win!")
        return "You win!"

number = randint(1, 100)

# my_guess = let_me_guess()

check_the_value(number, let_me_guess())
