# -*- coding: utf-8 -*-
"""
Programming 6 Template

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Gabriel Dell
"""
__version__ = 1

def caughtSpeeding(speed, isBirthday):    
    '''
    Write a function in Python that implements the following logic: You are driving a little
    too fast, and a police officer stops you. Write code to compute the result, encoded as an
    int value: 0=no ticket, 1=small ticket, or 2=big ticket. If speed is 60 or less, the
    result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or
    more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher
    in all cases.
    '''
    if isBirthday == True:
        if speed <= 65:
            return 0
        elif 66<=speed<=86:
            return 1
        elif speed > 86:
            return 2
    else:
        if speed <= 60:
            return 0
        elif speed > 61 or speed <= 80:
            return 1
        else:
            return 2



def noTeenSum(a, b, c):
    '''
    Write a function in Python that implements the following logic: Given 3 int values, a, b,
    and c, return their sum. However, if any of the input values is a teen -- in the range 13..19
    inclusive--then that value counts as 0, except that 15 and 16 do not count as teens.
    '''
    for i in range(13, 15):
        if a == i:
            a = 0
        elif b == i:
            b = 0
        elif c == i:
            c = 0
    for i in range(17, 20):
        if a == i:
            a = 0
        elif b == i:
            b = 0
        elif c == i:
            c = 0 
            
    summation = a + b + c
    print(summation)
    return summation


######################################################################################

def main():
    # You can test your solutions by calling them from here
    noTeenSum(15, 15, 10)
    noTeenSum(16,16,5)
    noTeenSum(12,1,12)
    noTeenSum(16,17,18)
    noTeenSum(17,1,2)
   
if __name__ == "__main__":
    main()    