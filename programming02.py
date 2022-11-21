# -*- coding: utf-8 -*-
"""
Programming 2 template

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Gabriel Dell
"""
__version__ = 1

def squirrelPlay(temperature, isSummer):    
    '''
    Write a function in Python that implements the following logic: The squirrels in Palo Alto 
	spend most of the day playing. In particular, they play if the temperature is between 
	60 and 90 (inclusive), unless it is summer, in which case the upper limit is 100 instead of 90. 
	Given an integer temperature and a Boolean isSummer, return True if the squirrels play 
	and False otherwise.
    '''
    if isSummer == True and temperature <= 100 and temperature >= 60:
        return True
    elif isSummer == False and temperature >= 60 and temperature <= 90:
        return True
    else:
        return False


def blackjack(a,b):
    '''
	Write a function in Python that implements the following logic: Given 2 int values a and b 
	greater than 0, return whichever value is nearest to 21 without going over. Return 0 if they 
	both go over.
	'''
    
    #excluded_value = 21
    if a <= 21 and b > 21:
        return a
    elif a > 21 and b <= 21:
        return b
    elif a <= 21 and b <= 21:
        a_count = 21 - a
        b_count = 21 - b
        if a_count < b_count:
            return a
        elif b_count < a_count:
            return b
        elif b_count == a_count:
            return a_count - 1
    else:
        return 0
        


######################################################################################

def main():
    # You can test your solutions by calling them from here
    print(squirrelPlay(100, True))
    print(squirrelPlay(60, True))
    print(squirrelPlay(90, False))
    print(squirrelPlay(60, False))
    print(squirrelPlay(120, False))
    #################################
    print(blackjack(22,22))
    print(blackjack(20, 12))
    print(blackjack(30, 12))
    print(blackjack(12, 40))
    print(blackjack(10, 15))
    print(blackjack(10,10))
if __name__ == "__main__":
    main()    