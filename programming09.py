# -*- coding: utf-8 -*-
"""
Programming 9 Template

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Gabriel Dell
"""
__version__ = 1

def theEnd(string,front):    
    '''
    Write a function in Python that implements the following logic: Given a string, return a
    string of length 1 from its front, unless front is false, in which case return a string
    of length 1 from its back. The input string will be non-empty.
    '''
    if front == True:
        return string[0]
    elif front == False:
        return string[-1]
    else:
        return False





def evenlySpaced(a,b,c):
    '''
    Write a function in Python that implements the following logic: Given three integers,
    a, b, and c, one of them is small, one is medium, and one is large. Return True if the three
    values are evenly spaced, so the difference between small and medium is the same as the
    difference between medium and large.  Return False otherwise.
    '''
    if (a==b) and (b==c):
        return True
    if(a==b) or (a==c) or (b==c):
        return False
    diff1 = abs(a-b)
    diff2 = abs(a-c)
    diff3 = abs(b-c)
    
    if (diff1 == diff2):
        return True
    if (diff1 == diff3):
        return True
    if (diff2 == diff3):
        return True
    else:
        return False
    
    

######################################################################################

def main():
    # You can test your solutions by calling them from here
    print(theEnd('Hi', True))
    print(theEnd('Hello', False))
    print(theEnd('oh', True))
    print(evenlySpaced(2,4,6)) # True
    print(evenlySpaced(4,6,2)) # True
    print(evenlySpaced(4,6,3)) # False
   
if __name__ == "__main__":
    main()    