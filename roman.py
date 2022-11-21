# -*- coding: utf-8 -*-
"""
Detect valid Roman numerals

Refer to the instructions on Canavs for more information.

"I have neither given nor received help on this assignment."
author: Gabriel Dell
"""
__version__ = 1

def valid_numeral(test_case):
    # Here is where you will write your function to determine
    # the validity of a string input
    valid_numerals = {'I':1, 'V':5, 'X':10,'L':50,'C':100,'D':500,'M':1000}
    test_set = ["I",'V', "X", "L", "C", 'D', "M"]
    power_10 = ['I', "X", "C", "M"]
    
    #If empty returns False or just has one characters returns True
    if len(test_case) == 0:
        return False
    elif len(test_case) == 1:
        return True
        
    #Rule1
    # Iterates through the test_case and if any character is not uppercase, returns False
    for char in range(len(test_case)):
        if test_case[char].isupper() == False:
            return False
        else:
            pass
        
    #Rule 2
    #Trying to take values from a dictionary character and compare to each test case letter
    for i in range(len(test_case)):
        if test_case[i] in test_set:
            #Going through the dictionary keys and seeing if any letters in the test_case are equivalent
            for key in valid_numerals.keys():
                if test_case[i] == key:
            
                    #Rule 3
                    #Tests to see if there are 4 characters in a row, if so, returns False
                    if str(test_case) == str(key*4):
                        return False
                    else:
                        break
        else:
            return False
        
    #Valid numerals, goes through the keys in the dictionary and if any letter is equivalent, finds the value and
    #appends it to a list
    numbers = []
    for x in range(len(test_case)):
        for key in valid_numerals.keys():
                #print(test_case[i])
            if test_case[x] == key:
                tests = valid_numerals[key]
                numbers.append(tests)
            else:
                pass
    
            
    #Rule 5 and 6
    Rule5_6(valid_numerals, power_10, numbers, test_set, test_case)
    
    return Rule5_6(valid_numerals, power_10, numbers, test_set, test_case) 
##############################
def Rule6(test_case, test_set):
    nums = []
    for i in range(len(test_case)):
        #Taking in test_case and comparing to a test_set, which is a set of characters of roman numerals
        for k in range(len(test_set)):
            #Tests if any letter in test_set is equal to the letter in the test_case, the smaller symobl letter
            if str(test_case[i]) == str(test_set[k]):
#Appends to a list called nums, and appends k in from the test_set which is, ["I",'V', "X", "L", "C", 'D', "M"]
                nums.append(k)
            else:
                pass
            
#After iterating, checks to see if the numbers in list nums is greater than 2, if so returns False, else returns True
#Creates a running sum.
    #print(nums)
    for i in range(len(nums)-1):
        #number += nums[i]
        if nums[i] - nums[i+1] > 2 or nums[i+1] - nums[i] > 2:
            return False
        else:
            pass
    return True
#############################         
def Rule5_6(valid_numerals, power_10, numbers, test_set, test_case):
    #If in the numbers list, the first number is greater than the seccond, move on to rule 7
    for i in range(len(numbers)-1):
       
        # Rule 4, checks to see if larger value is succeeded by a smaller value
        if numbers[i] > numbers[i+1] or numbers[i] == numbers[i+1]:
                #Checks to see if the letter in test case, is in a dictionary called power_10 that contains only power of 10
                #characters
            for i in range(len(test_case)-1):
                #If so then move on to rule 7, where it iterates through a dictionary and checks to see if the 
                #the letter *2 or *3 is the test_case, if so, it is valid, else return False.
                
                #Rule 7    
                if str(test_case[i] * 3) == str(test_case) or str(test_case[i] * 2) == str(test_case):
                    if str(test_case[i]) in power_10:
                        return True
                    else:
                        return False
                else:
                    pass
        #Rule 5
        #If smaller value is infront of a bigger number, checks that.
        elif numbers[i] < numbers[i+1]:
            for i in range(len(test_case)-1):
                #For loop goes through the test case and if the first letter(smaller value symbol) isn't in power_10
                #Return False, else go through
                if test_case[0] in power_10:
                    
                    #Checks to see if it is a power of 10, goes into rule 6 to check validity.
                    return Rule6(test_case, test_set)
                        
                else:
                    return False
                
        # else:
        #     return False
        
    return True
                    
                    
############################################################################################        


def main():
    # Here is where you will call your test cases
    #print(valid_numeral('Iv'))
    print(valid_numeral('IV'))
    print(valid_numeral("IX"))
    print(valid_numeral('VI'))
    print(valid_numeral('VX'))
    print(valid_numeral('LLL'))
    print(valid_numeral('XXX'))
    print(valid_numeral('M2C'))
    print(valid_numeral(''))
    print(valid_numeral('ADSF'))
    print(valid_numeral('I'))
    print(valid_numeral('IVD'))
    test1()
    testN()
    print("ALL TESTS PASSED")



###############################################################

# Here is where you will write your test case functions
    
# Below are the tests for Rule 1, validating that the string contains only characters
def test1():
    #Test1() is testing for everything
    assert valid_numeral("Iv") == False, "A lowercase letter should be capitalized"
    assert valid_numeral("IV") == True, "Should be true"
    assert valid_numeral('I') == True, "Should be True, I is a roman numeral"
    assert valid_numeral("iV") == False, "A lowercase 'i' was found, should be I."
    assert valid_numeral('VI') == True, "This should return True, bigger number is first, thus is true"
    assert valid_numeral("IC") == False, "This should be False, as rule 6 states it should be within one or two of the big symbol"
    assert valid_numeral("IX") == True, "X is within 2 of I and thus passes rule 5 and 6"
    assert valid_numeral("IL") == False, "L is not within 2 of I, failed rule 6 and didn't get False"
    assert valid_numeral("LC") == False, "L is within 2, a power of 10 and passes rules 5 and 6, didn't get True"
    assert valid_numeral('XVIII') == True, "Value greater than next value, didn't get True"
    assert valid_numeral("MCXIV") == True, "M > C, thus should have returned True"
    assert valid_numeral('CCCC') == False,  "CCCC is a roman numeral of 4 in a row, didn't return False"
    assert valid_numeral("CIL") == False, "C is not within 2 of I, should return False, didn't"

# def test2():
#     # This comment explains what test2() is testing for, and is followed by code
#     

# # Below are the tests for Rule 2, .....
def testN():
#     #testN() is testing for random things such as names or triple letters, and is followed by code
     assert valid_numeral("BIGM") == False, "Random letters, didn't return False"
     assert valid_numeral("XXXTENTACTION") == False, "The name of a rapper, didn't return False for being a roman numeral"
     assert valid_numeral("EMC2") == False, "The equation for general relatively, didn't return False as the letters don't exist"
     assert valid_numeral("VX") == False, "V isn't a power of 10, didn't return False"
     assert valid_numeral("II") == True, "2 in a row is true for rule 7, didn't return True though"
     assert valid_numeral("III") == True, "3 in a row, should be True, didn't get it though"
     assert valid_numeral("LLL") == False, "Though 3 in a row, is not a power of 10, didn't return False"
     assert valid_numeral("XXX") == True, "Is 3 in a row and a power of 10, didn't return True"
     assert valid_numeral("ASDF") == False, "Letters aren't in dictionary, should return False, didn't though"

    
    


    
###############################################################    
    
if __name__ == "__main__":
    main()    