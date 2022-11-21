# -*- coding: utf-8 -*-
"""
Programming 3 Template

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Gabriel Dell 
"""
__version__ = 1

def prefixAgain(string, N):    
    '''
    Given a string, consider the prefix made of the first N chars of the string. Does that
	prefix string appear somewhere else in the string?  Assume that the string is not empty 
	and that N is in the range 1..str.length(). Case is important to the existence of a prefix.
    '''
    prefix  = string[:N]
    #print(prefix)
    if prefix in string[N:]:
        return True
    else:
        return False



def greenTicket(a, b, c):
    '''
	You have a green lottery ticket with three integers: a, b, and c.  If all of the numbers 
	are different on it, return 0.  If two of the numbers are the same, return 10.  If all of 
	the numbers are the same, return 20.
	'''
    if a != b and a != c:
        return 0
    elif (a == c) and (a != b) or (a == b) and (a != c):
        return 10
    else:
        return 20



######################################################################################

def main():
    # You can test your solutions by calling them from here
    print(greenTicket(10,10, 9))
    print(greenTicket(20,20,20))
    print(greenTicket(3,4,5))
    print('This is', greenTicket(0,1,1))
    print(greenTicket(1,2,1))
    print(prefixAgain('prefix', 3))
    print(prefixAgain('triangle', 3))
   
if __name__ == "__main__":
    main()    