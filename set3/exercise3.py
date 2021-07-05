"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""


def super_asker(low, high, message):
    while True:
        try:
            ask_for_number = int(input(message))
            print(f"{ask_for_number} is a number")
            if low < ask_for_number < high:
                return ask_for_number
        except Exception as e:
            print(f"{e} is not a number")


def advancedGuessingGame():
    """Play a guessing game with a user.
    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")

    lowerBound = super_asker(-1000, 1000, "Enter a lower bound: ")
    upperBound = super_asker(lowerBound + 1, 1000, "Enter an upper bound: ")

    actualNumber = random.randint(lowerBound + 1, upperBound - 1)

    while True:
        guessedNumber = super_asker(
            lowerBound,
            upperBound,
            f"Guess a number between {lowerBound} and {upperBound}: ",
        )
        print("The number you guessed is {},".format(guessedNumber))
        if guessedNumber == actualNumber:
            print("You guessed it!! It was {}".format(actualNumber))
            return "You got it!"
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        elif guessedNumber > actualNumber:
            print("Too big, try again :'(")


# the tests are looking for the exact string "You got it!". Don't modify that!

if __name__ == "__main__":
    print(advancedGuessingGame())
