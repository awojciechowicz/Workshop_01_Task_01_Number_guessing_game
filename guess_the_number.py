from random import randint

def let_me_guess():
    """Let user guess the number.

    Try until user gives a proper number.

    :rtype: int
    :return: given number as int
    """
    while True:
        try:
            guess = int(input("Guess the number: "))
            return guess
        except ValueError:
            print("It's not a number")

def check_the_value():
    """Main function"""
    number = randint(1, 100)
    print(number)
    while True:
        my_guess = let_me_guess()
        if my_guess < number:
            print("Too small!")
        elif my_guess > number:
            print("Too big!")
        elif my_guess == number:
            return "You win!"


print(check_the_value())