# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 11:53:43 2022

@author: gabel
"""

# -*- coding: utf-8 -*-
"""
Programming 10 Template

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Gabriel Dell
"""
__version__ = 1

class NumberStorage:

    '''
    The data parameter will contain a non-empty list of integers.
    '''
    def __init__(self, data):
        self.__data = data
        self.__min = 0
        
    def getMin(self):
        return self.__min
        
    def findMax(self):
        '''
        Objects that are created from this NumberStorage class will be initialized with a
        list of integers that are stored in self.__data.  This method will identify and
        RETURN the largest value in that list.
        '''
        running_sum = 0
        data = self.__data
        for i in range(len(data)):
            if data[i] > running_sum:
                running_sum = data[i]
            else:
                pass
        return running_sum
    
    def findMin(self):
        '''
        This method will identify the smallest number in the self.__data list, and then
        will STORE that value into self.__min.  (The value will then be accessible using
        the getMin() method.
        '''
        running_sum = 0
        data = self.__data
        for i in range(len(data)):
            running_sum = data[0]
            if data[i] < running_sum:
                running_sum = data[i]
            else:
                pass
        self.__min = running_sum
        


######################################################################################

def main():
    # You can test your solutions by calling them from here
    '''
    Here is an example of a test that you can write for findMax:
        data = [1,2,3,4,5]
        testObj = NumberStorage(data)
        assert testObj.findMax() == 5, "The largest value in [1,2,3,4,5] is 5."
        
    Here is an example of a test that you can write for findMin:
        data = [1,2,3,4,5]
        testObj = NumberStorage(data)
        testObj.findMin()
        assert testObj.getMin() == 1, "The smallest value in [1,2,3,4,5] is 1."
    '''
    data = [1,2,3,4,5]
    testObj = NumberStorage(data)
    assert testObj.findMax() == 5, "The largest value in [1,2,3,4,5] is 5."
    
    data = [1,2,3,4,5]
    testObj = NumberStorage(data)
    testObj.findMin()
    assert testObj.getMin() == 1, "The smallest value in [1,2,3,4,5] is 1."
    print('ALL TESTS PASSED')
   
if __name__ == "__main__":
    main()    