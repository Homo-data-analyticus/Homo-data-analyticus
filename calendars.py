# -*- coding: utf-8 -*-
"""
Functions about calendars

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Gabriel Dell

Conceptually this is put supposed to make a gregorian and a milankovic calendar
so that any year can be processed in either and return whether or not it is a 
leap year and equally you can put in a selection of ranges of years that allow
for the total number of leap years in between 2 different years.
"""
__version__ = 1

def gregorian(year):
    # Here is where you will write your function to determine
    # if a year is a Gregorian leap year
    
    # year is divisible by 4, it goes on, else it isn't a leap year
    if year % 4 == 0:
        # if divisible by 100, it isn't a leap year, if it isn't, it is, thus
        #helping explain the reversal in the true or false return statements.
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    


def milankovic(year):
    # Here is where you will write your function to determine
    # if a year is a Milankovic leap year
    
    #Same concept for the milankovic calendar, if year perfectly divisible by
    # 4, then it moves on, else returns False.
    if year % 4 == 0:
        if year % 100 == 0:
            # If the year is being divided by 900 and the remainder is either
            # 200 or 600, then it is a leap year, else it is not
            if year % 900 == 200 or year % 900 == 600:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        


def gregorian_count(year1, year2):
    # Here is where you will write your function to determine
    # the number of leap years that lie between two dates on
    # the Gregorian calendar
    
    #Leap_year_total is a counter to keep track of the number of leap years
    # between 2 dates
    leap_year_total = 0
    # Has a range between the 2 dates and adds 1 for the range function because
    # range inherently subtracts 1 off the end
    for specific_year in range(year1, year2):
        # calls the gregorian function of year with the argument being the specific
        # year from the for loop to determine each individual year and if that is 
        # true, then add one to the counter
        if gregorian(specific_year) == True:
            leap_year_total += 1
        #else:
            #pass
    return leap_year_total


def milankovic_count(year1, year2):
    # Here is where you will write your function to determine
    # the number of leap years that lie between two dates on
    # the Milankovic calendar
    
    #Literally the same exact thing, except this for the milankovic calendar
    leap_year_total = 0
    for specific_year in range(year1, year2):
        if milankovic(specific_year) == True:
            leap_year_total += 1
        #else:
            #pass
        
    return leap_year_total


def main():
    # Here is where you will call your test cases
    test1()
    test2()
    testN()
    print("ALL TESTS PASSED")



###############################################################

# Here is where you will write your test case functions
    
# Below are the tests for gregorian()
def test1():
    # Test 1 is for the function gregorian, to help determine if the gregorian
    # year is in fact a leap year, should return True or False
    assert gregorian(1696) == True, "Passing in 1696, didn't return True"
    assert gregorian(1697) == False, "Passing in 1697 didn't return False"
    assert gregorian(2100) == False, "Passing in 2100 didn't return False"
    assert gregorian(1900) == False, "Passing in 1900 didn't return False"
    

def test2():
    # Test 2 is about gregorian leap years and the total between 2 ranges of years, in which 
    # the first year is greater than the second year.
    assert gregorian_count(1696, 1697) == 1, "Passing in 1696 to 1697 didn't return 1 leap year"
    assert gregorian_count(1900, 1901) == 0, "Passing in 1900 to 1901 didn't return 0 leap years"
    assert gregorian_count(2000, 3000) == 243, "Passing in 2000 to 3000, didn't return 243 leap years"
    assert gregorian_count(2000, 2850) == 207, "Passing in 2000 to 2850 didn't return 207 leap years"
    assert gregorian_count(2020, 10000) == 1935, "Passing in 2020 to 10000 didn't return 1935 leap years"
    assert gregorian_count(20, 2020) == 485, "Passing in 20 to 2020 didn't return 485 leap years"

# Below are the tests for milankovic()
def testN():
    # Test N is about milankovic system of the calendar, it is supposed to determine, whether again
    # a certain year inputted as an argument into milankovic, is a leap year.
    # To be honest, the only difference from the gregorian calendar
    #comes after I'm dead, so.... yeah.
    assert milankovic(1696) == True, "Passing in 1696 to the milankovic calendar didn't return True"
    assert milankovic(1697) == False, "passing in 1697 into the milankovic calendar didn't return False"
    assert milankovic(2100) == False, "Passing in 2100 into the milankovic calendar didn't return False"
    assert milankovic(2800) == False, "Passing in 2800 into the milankovic calendar didn't return False"
    assert milankovic(1900) == False, "Passing in 1900 into the milankovic calendar didn't return False"
    ##########################
    assert milankovic_count(1696,1697) == 1, "Passing in 1696 to 1697 in the milankovic calendar didn't return 1 leap year"
    assert milankovic_count(1900, 1901) == 0, "Passing in 1900 to 1901 in the milankovic calendar didn't return any leap years"
    assert milankovic_count(2000, 3000) == 243, "Passing in 2000 to 3000 in the milankovic calendar didn't return 243 leap years"
    assert milankovic_count(2000, 2850) == 206, "Passing in 2000 to 2850 in the milankovic calendar didn't return 206 leap years"
    
    
###############################################################    
    
if __name__ == "__main__":
    main()    