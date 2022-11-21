# -*- coding: utf-8 -*-
"""
Programming 7 Template

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Gabriel Dell
"""
__version__ = 1

def roundSum(a,b,c):    
    '''
    For this problem, we'll round an int value up to the next multiple of 10 if its
    rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to
    the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds
    down to 10. Given 3 integers, a, b, and c, return the sum of their rounded values.
    To avoid code repetition, write a separate helper function round10(num) and call
    it 3 times. The helper function definition is provided below.
    '''
    return round10(a) + round10(b) + round10(c)

def round10(num):
    '''
    This is where you will write the helper function as described above.
    '''
    
    return (num + 5)// 10 * 10

        
def makeChocolate(givenSmall, givenBig, goal):
    '''
    We want to make a package of goal kilos of chocolate. We have small bars
    (1 kilo each) and big bars (5 kilos each). Return the number of small bars
    to use, assuming we always use big bars before small bars to reach the total
    goal.  Return -1 if goal kilos can't be made with givenSmall small bars and
    givenBig big bars.  You cannot break a big bar into 5 small bars.
    '''
    
    if(givenSmall + givenBig*5 < goal):
        return -1
    elif givenSmall < goal%5:
        return -1
    else:
        if(goal<10): 
            return goal%5
    return goal-(givenBig*5)

######################################################################################

def main():
    # You can test your solutions by calling them from here
    print(roundSum(10, 16, 42))
    print(makeChocolate(8, 2, 18))
    print(makeChocolate(10, 2, 25))
if __name__ == "__main__":
    main()    