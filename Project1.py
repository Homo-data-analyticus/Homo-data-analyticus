# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 13:02:09 2022

@author: gabel
"""

"""
Practice with writing test cases and performing test-driven development using a
Guess-My-Number game as a problem statement.

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Gabriel Dell
"""
__version__ = 1

import random

def computerNumber():
    '''
    This function should generate a computer number in the 1-100 range, returning that value
    from the function.
    '''
    computer = random.randint(1,100)
    return computer

def userGuess():
    '''
    This function should obtain a guess from the user, validate that it is in the 1-100 range,
    and return that value from the function.
    '''    
    user =input("Please enter a number:")
    
    
    while user.isalpha() == True:
        print("Hey, that is a letter, try again")
        user = input("Please enter a number: ")
        if user.isdigit():
            user.isalpha() == False
            while int(user) > 100 or int(user) < 0:
                print("The number choosen is not the selected range, please try again")
                user = input("Please enter a number:")
    #else:
        #user = input("Please enter a number between 1 and 100: ")
    
    
    return int(user)
        


def provideFeedback(user, computer):
    '''
    This function should take as inputs the guess from the user and the number from the computer,
    and will provide feedback as to whether the user's guess is too low, too high, or correct.
    '''
    if user > computer:
        high_str = 1
        return high_str
    elif user == computer:
        correct_str = 0
        return correct_str
    elif user < computer:
        low_str = -1
        return low_str
        

def gameLoop():
    '''
    This function handles the main game loop, continually calling the userGuess() and
    provideFeedback() functions until the user guesses correctly.  After the user has guessed
    correctly, this function will return 0.
    '''
    
    computer_number = computerNumber()
    while (output := provideFeedback(userGuess(), computer_number)) != 0:
        #print(output)
        if output == -1:
            print("The number is to low")
        elif output == 1:
            print("The number is to high")
    return 0
    quit()

def main():
    # Here is where you will call your test cases
    testGeneratedNumber()
    testRange()
    testGuessInteger()
    testGuessHigh()
    testGuessLow()
    testGuessRight()
    testGameEnd()
    print("All TEST PASSED") 
    print("Thanks for playing the game")
    quit()


###############################################################

# Here is where you will write your test case functions
     
def testGeneratedNumber():
    for i in range(1000):
        assert computerNumber() >= 1 and computerNumber() <= 100, "The computer generated a number out of range"
def testRange():
    assert userGuess() >= 1 and userGuess() <= 100, "The users guess is not in the range"
def testGuessInteger():
    assert type(userGuess()) == type(int()), "The users guess is not a integer data type"
def testGuessHigh():
    computer_number = computerNumber()
    print(computer_number)
    assert provideFeedback(userGuess(), computer_number) == 1, "The number is to high"
def testGuessLow():
    computer_number = computerNumber()
    print(computer_number)
    assert provideFeedback(userGuess(), computer_number) == -1, " The number is to low"
def testGuessRight():
    computer_number = computerNumber()
    print(computer_number)
    assert provideFeedback(userGuess(), computer_number) == 0, "This error means, that the guess and the random number arent the same"
def testGameEnd():
    assert gameLoop() == 0, "The game should end"

###############################################################    
    
if __name__ == "__main__":
    main()    