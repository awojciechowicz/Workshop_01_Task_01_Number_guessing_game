from random import randint

number = randint(1, 100)

while True:
    guess = input("Guess the number: ")
    try:
        guess = float(guess)
        break
    except ValueError:
        print("It's not a number")