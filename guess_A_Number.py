import random
import sys

def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print('You Entered a character! Try again pls..')
            continue
        else:
            return userInput
            break

def guessNumber():
    number=random.randint(1,40)
    count=1
    guess= inputNumber("Enter your guess between 1 and 40: ")

    while guess !=number:
        count+=1
        if guess > (number + 10):
            print("Too high!")
        elif guess < (number - 10):
            print("Too low!")
        elif guess > number:
            print("Getting warm but still high!")
        elif guess < number:
            print("Getting warm but still Low!")

        guess = int(input("Try again "))

    if guess == number:
        print("Well played! You guessed the number in ", count, " tries!")


    again = str(input("Want another try? (yes/no): "))
    if again == "yes":
        guessNumber()
    else:
        print('thanks for playing..Goodbye')
        sys.exit(0)

guessNumber()


