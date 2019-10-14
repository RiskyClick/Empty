#! python3
#Nubmer guessing game.

import random

def playAgain():
    print("Want to play again?")
    while(True):
        playAgain = input()
        if(playAgain == "yes"):
            guessingGame(userName)
        elif(playAgain == "no"):
            print("Thanks for playing")
            False
            break
        else:
            print("what?")
    exit(0)


def guessingGame(userName):
    print("Im thinking of a number between 1 and 100")
    print("You have 10 chances to guess it")
    print("Enter 'quit' if your done")
    numberToGuess = random.randint(0, 101)#random number between 1 and including 100
    numberOfGuesses = 0
    while(numberOfGuesses < 10):
        numberOfGuesses = numberOfGuesses + 1
        guess = input()
        if(numberOfGuesses == 10):
            print("YOU LOOSE!!!")
            playAgain()
        if(guess.isalpha() == True):#check to see if enered quit
            if(guess == "quit"):
                print("Thanks for playing!")
                exit(0)
            else:
                print("Not valid entry, try again!")
                print(str(10 - numberOfGuesses) + " guesses remain")
        else:
            try:
                guess = int(guess)           
                if(guess < numberToGuess):
                    print("Sorry " + userName + ", guess higher")
                    print(str(10 - numberOfGuesses) + " guesses remain")
                elif(guess > numberToGuess):
                    print("Sorry " + userName + ", guess lower")
                    print(str(10 - numberOfGuesses) + " guesses remain")
                elif(guess == numberToGuess):
                    print("Congrats " + userName + "! You got it right in: " + str(numberOfGuesses) + " guesses!")
                    playAgain()                       
            except ValueError:
                print("Not valid entry, try again!")
                print(str(10 - numberOfGuesses) + " guesses remain")
                continue
    
print("Welcome to the number guessing game.")#beging of program start here
print("Whats your name?")
userName = str(input())
if(userName.isalpha() == False):
    print("weird name but okay")
guessingGame(userName)


