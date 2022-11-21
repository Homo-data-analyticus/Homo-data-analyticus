# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 08:57:45 2022

@author: gabel
"""

#######################################################
# function, main

def calculator(strNumbers):
    if strNumbers == '':
        return 0
    
    strNumbers = fixSemicolons(strNumbers)
    
    numberList = strNumbers.split(',')

    mySum = 0
    for i in range(len(numberList)):
        mySum += float(numberList[i])
    return mySum

def fixSemicolons(semicolonString):
    return semicolonString.replace(';', ',')

def fixUniqueDelimiter(strNumbers):
    delimiter = strNumbers[0]
    everythingElse = strNumbers[1:]
    return everythingElse.replace(delimiter, ',')

def main():
    testSingleNumber()
    testEmptyString()
    testAddingZero()
    testManyInputs()
    testManyNegatives()
    testSemicolonDelimiter()
    testUniqueDelimiters()
    print("ALL TESTS PASSED")



#######################################################
# tests

def testSingleNumber():
    assert calculator("6") == 6, "Passing the string 6 into calculator didnt return 6."
    assert calculator("-6") == -6, "Passing the string -6 into calculator didnt return -6."
    assert calculator("0") == 0, "Passing the string 0 into calculator didnt return 0."
    assert calculator("12345") == 12345, "Passing the string 12345 into calculator didnt return 12345."
    assert calculator("1.23") == 1.23, "Passing the string 1.23 into calculator didnt return 1.23."

def testEmptyString():
    assert calculator("") == 0, "Passing an empty string into calculator didnt return 0"

def testAddingZero():
    assert calculator("6, 0") == 6, "Passing the string 6, 0 into calculator didnt return 6,0."
    assert calculator("0, 6") == 6, "Passing the string 0, 6 into calculator didnt return 6,0."
    assert calculator("-6, 0") == -6, "Passing the string -6, 0 into calculator didnt return -6."
    assert calculator("0, 0") == 0, "Passing the string 0,0 into calculator didnt return 0."
    assert calculator("12345, 0") == 12345, "Passing the string 12345,0 into calculator didnt return 12345."
    assert calculator("1.23, 0") == 1.23, "Passing the string 1.23,0 into calculator didnt return 1.23."

def testManyInputs():
    assert calculator("1,2,3,4,5,6,7,8") == 36, "Passing numbers 1-8 into calculator, didn't return 36"
    assert calculator("1,2,3,4,5,6") == 21, "Passing numbers 1-6 into calculator, didn't return 21"
    assert calculator("1,2,3,4,5") == 15, "Passing numbers 1-5 into calculator, didn't return 15"
    assert calculator("4,5,6,7,8") == 30, "Passing numbers 4-8 into calculator, didn't return 30"
    assert calculator("1,2,0,4,5,0,7,8") == 27, "Passing numbers 1,2,0,4,5,0,7,8 into calculator, didn't return 27"
    assert calculator("-1,2,0") == 1, "Passing numbers 0,-1,2 into calculator, didn't return 1"

def testManyNegatives():
    assert calculator("-1,-2,-3,4,-5,-6,-7,-8") == -28, "Passing numbers 1-8 into calculator, didn't return -32"
    assert calculator("-1,-2,-3,4,-5,-8") == -15, "Passing numbers -1,-2,-3,4,-5,-8 into calculator, didn't return -16"
    assert calculator("-4,-5,-6,-7,-8") == -30, "Passing numbers -4,-5,-6,-7,-8 into calculator, didn't return -32"

def testSemicolonDelimiter():
    assert calculator("1;2;3;4;5;6;7;8") == 36, "Passing the string '1;2;3;4;5;6;7;8' into calculator() didn't return 36"
    assert calculator("1;2;3;4;5;6") == 21, "Passing the string '1;2;3;4;5;6' into calculator() didn't return 21"
    assert calculator("1;2;3;4;5") == 15, "Passing the string '1;2;3;4;5' into calculator() didn't return 15"
    assert calculator("4;5;6;7;8") == 30, "Passing the string '4;5;6;7;8' into calculator() didn't return 30"
    assert calculator("1,2,0;4,5,0,7;8") == 27, "Passing the string '1,2,0;4,5,0,7;8' into calculator() didn't return 27"
    assert calculator("-1;2,0") == 1, "Passing the string '-1;2,0' into calculator() didn't return 1"
    assert fixSemicolons("1;2;3") == "1,2,3", "Passing the string '1;2;3' into fixSemicolons() didn't return '1,2,3'"
    assert fixSemicolons("1,2;3") == "1,2,3", "Passing the string '1,2;3' into fixSemicolons() didn't return '1,2,3'"

def testUniqueDelimiters():
    assert calculator("w1w2w3w4w5") == 15, "Passing the string 'w1w2w3w4w5' into calculator() didn't return 15"
    assert calculator("^4^5^6^7^8") == 30, "Passing the string '^4^5^6^7^8' into calculator() didn't return 30"
    assert calculator("-4,-5,-6,-7,-8") == -30, "Passing the string '-4,-5,-6,-7,-8' into calculator() didn't return -30"
    assert fixUniqueDelimiter("w1w2w3w4w5") == "1,2,3,4,5", "Passing the string 'w1w2w3w4w5' into fixUniqueDelimiter() didn't return '1,2,3,4,5'"

#######################################################
# potentially run main


if __name__ == '__main__':
    main()






#######################################################