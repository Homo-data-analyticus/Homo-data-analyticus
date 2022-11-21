# -*- coding: utf-8 -*-
"""
Programming 8 Template

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Gabriel Dell
"""
__version__ = 1

def dateFashion(you, date):    
    '''
    (Before COVID), you and your date were trying to get a table at a restaurant. The parameter
    you is the stylishness of your clothes, in the range 0..10, and date is the stylishness of
    your date's clothes. Write a method that returns your chances of getting a table, encoded as
    an int value with 0 = no, 1 = maybe, 2 = yes. If either one of you is very stylish, 8 or more,
    then the result is 2 (yes). But this decision is overridden if the other date participant
    has style of 2 or less, in which case the result is 0 (no). Otherwise the result is 1 (maybe).
    '''
    if you <= 2 or date <= 2:
        return 0
    elif you > 8 or date > 8:
        return 2
    else:
        return 1



def mixString(a, b):
    '''
    Write a function in Python that implements the following logic: Given two strings, a and b,
    create a bigger string made of the first character of a, the first character of b, the second
    character of a, the second character of b, and so on. Any leftover characters go at the end of
    the result.
    '''
    string = ''
    i = 0
    while (i < len(a)) or (i < len(b)):
        
        if (i < len(a)):
            string += a[i]
        if (i < len(b)):
            string += b[i]
        
        i += 1
        
    return string

######################################################################################

def main():
    # You can test your solutions by calling them from here
    print(dateFashion(5, 10))
    print(dateFashion(5, 2))
    print(dateFashion(5, 5))
    print(mixString('Hi', 'Hi'))
    print(mixString('Acb', 'Xyz'))
   
if __name__ == "__main__":
    main()    