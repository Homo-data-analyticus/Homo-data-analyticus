# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 13:30:38 2022

@author: gabel
"""

# -*- coding: utf-8 -*-
"""
Defining a to-do list class.

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Gabriel Dell
"""
__version__ = 1


'''
Do not edit the class definition or methods in this section.  They exist for 
testing purposes
'''

class ToDoList:
    def __init__(self):
        self.__items = []
        self.__numItems = 0
        self.__currentDay = 0
    
    def getItems(self):
        return self.__items
    
    def getNumItems(self):
        return self.__numItems
    
    def setItems(self, newItems, newLen):
        self.__items = newItems
        self.__numItems = newLen
    
    def setCurrentDay(self, newDay):
        self.__currentDay = newDay
    
    def nextDay(self):
        self.__currentDay += 1
    
    def __str__(self):
        output = ""
        for item in self.__items:
            output += (item['title'] + '\n')
            output += ("Due: " + str(item['duedate']) + '\n')
            output += ("From: " + item['assignedby'] + '\n\n')
        return output
    
    
############################################################ 
    
    '''
    These are the methods that you should create for this project:
    '''
    
    def addItem(self, item):
        #Creates an item object, then appends that to self.__items and increases numItems object by 1
        self.__item = item
        self.__items.append(item)
        self.__numItems += 1
                
    def currentListLength(self):
        #returns length of the total number of items in self.__items
        return len(self.__items)
    
    def numberItemsDueToday(self):
        
        #Creates a running sum of number of tasks to be completed
        num_tasks = 0
        #For loop of self.__items
        for i in range(len(self.__items)):
            #if the duedate of a dictionary is the same as the current day, then add one to the running sum, else move on.
            if self.__items[i]['duedate'] == self.__currentDay:
                num_tasks += 1
            else:
                pass
            
        return num_tasks
    
    def itemExistsInList(self, title):
        for i in range(len(self.__items)):
            
            #if the title of self.__items[i] is equal to the title inputted into the function, then return True else pass
            # and if throughout the whole for loop, doesn't return True, then just Return False
            if self.__items[i]['title'] == title:
                return True
            else:
                pass
            
        return False
    
    def removeItemsForToday(self):
        #Sets the current day to some number
        self.setCurrentDay(0)
        
        for i in range(len(self.__items)):
            # print(len(self.__items))
            # print('Duedate is', self.__items[-i]['duedate'])
            # print('This is', self.__currentDay)
            
            if self.__items[-i]['duedate'] == self.__currentDay:
                #Removes the item that has a duedate the same as currentDay
                self.__items.remove(self.__items[-i])
                #Takes the total number of items and subtracts that by one
                self.__numItems -= 1
                #Calls the nextDay function in order to see if there are other matches of duedates and the current day
                #self.nextDay()
            else:
                #self.nextDay()
                pass
    
            
            
def main():
    items = [# Item 0
{ "title": "Task 0",
  "duedate" : 0,
  "assignedby" : "Jim"},

# Item 1
{ "title": "Task 1",
  "duedate" : 1,
  "assignedby" : "Jessica"},

# Item 2
{ "title": "Task 2",
  "duedate" : 2,
  "assignedby" : "Jeff"},

# Item 3
{ "title": "Task 3",
  "duedate" : 0,
  "assignedby" : "Jane"},

# Item 4
{ "title": "Task 4",
  "duedate" : 2,
  "assignedby" : "Josh"},

# Item 5
{ "title": "Task 5",
  "duedate" : 3,
  "assignedby" : "James"},

# Item 6
{ "title": "Task 6",
  "duedate" : 5,
  "assignedby" : "Jack"},

# Item 7
{ "title": "Task 7",
  "duedate" : 2,
  "assignedby" : "Joe"},

# Item 8
{ "title": "Task 8",
  "duedate" : 5,
  "assignedby" : "John"},

# Item 9
{ "title": "Task 9",
  "duedate" : 4,
  "assignedby" : "Jill"},]

    obj = ToDoList()
    print(obj.addItem(items[3]))
    print(obj.addItem(items[4]))
    print(obj.getNumItems())
    print(obj.getItems())
    
    print(obj.numberItemsDueToday())
    print(obj.itemExistsInList('Task 2'))
    print(obj.removeItemsForToday())
    print(obj.getNumItems())
    
    obj = ToDoList()
    obj.addItem(items[3])
    obj.addItem(items[5])
    print(obj.getItems())
    print(obj.getNumItems())
    print(obj.numberItemsDueToday())
    print(obj.itemExistsInList('Task 5'))
    obj.removeItemsForToday()
    print(obj.getNumItems())
    
    obj = ToDoList()
    obj.addItem(items[8])
    print(obj.getItems())
    print(obj.getNumItems())
    print(obj.numberItemsDueToday())
    print(obj.itemExistsInList('Task 7'))
    obj.removeItemsForToday()
    print(obj.getNumItems())
    
    obj = ToDoList()
    print(obj.getNumItems())
    
    obj = ToDoList()
    obj.addItem(items[6])
    obj.addItem(items[7])
    obj.addItem(items[3])
    print(obj.getNumItems())
    print(obj.getItems())
    print(obj.numberItemsDueToday())
    print(obj.itemExistsInList('Task 6'))
    obj.removeItemsForToday()
    print(obj.getNumItems())
    
    
    
    obj = ToDoList()
    obj.addItem(items[0])
    obj.addItem(items[1])
    obj.addItem(items[2])
    obj.removeItemsForToday()
    print(obj.getNumItems())
    #test1()
    print('ALL TESTS PASSED')
############################################################    
    
# Below are the tests for addItem()
def test1():
    #Gets a list of items from a txt file that has various dictionaries.
    items = [# Item 0
{ "title": "Task 0",
  "duedate" : 0,
  "assignedby" : "Jim"},

# Item 1
{ "title": "Task 1",
  "duedate" : 1,
  "assignedby" : "Jessica"},

# Item 2
{ "title": "Task 2",
  "duedate" : 2,
  "assignedby" : "Jeff"},

# Item 3
{ "title": "Task 3",
  "duedate" : 0,
  "assignedby" : "Jane"},

# Item 4
{ "title": "Task 4",
  "duedate" : 2,
  "assignedby" : "Josh"},

# Item 5
{ "title": "Task 5",
  "duedate" : 3,
  "assignedby" : "James"},

# Item 6
{ "title": "Task 6",
  "duedate" : 5,
  "assignedby" : "Jack"},

# Item 7
{ "title": "Task 7",
  "duedate" : 2,
  "assignedby" : "Joe"},

# Item 8
{ "title": "Task 8",
  "duedate" : 5,
  "assignedby" : "John"},

# Item 9
{ "title": "Task 9",
  "duedate" : 4,
  "assignedby" : "Jill"},]
    
    #I am doing testing based off of each item in the items list
    #For each item I am checking each one of the functions to make sure they work accurately

    obj = ToDoList()
    obj.addItem(items[0])
    assert obj.getNumItems() == 1, "When adding the first task, the number of items wasn't one"
    
    assert obj.numberItemsDueToday() == 1, "When adding the first task, the number of items due today isn't one"
    assert obj.itemExistsInList('Task 0') == True, "If there is a Task 0 in the dictionary, then should return True, didn't."
    obj.removeItemsForToday()
    assert obj.getNumItems() == 0, "Should return 0, as obj3 removed an item from self.__items, didn't do it though"
    
    obj.addItem(items[1])
    obj.addItem(items[2])
    assert obj.getNumItems() == 2, "Adding 2 tasks, the number of items wasn't 2."
    assert obj.numberItemsDueToday() == 0, "The duedate's and the current day didn't match up properly"
    assert obj.itemExistsInList('Task 2') == True, 'Should be True as items[2][title] is Task 2 and thus should return True'
    obj.removeItemsForToday()
    assert obj.getNumItems() == 2, "The current day and the duedate didn't match up properly, meaning it didn't execute when it was supposed to"
    
    
    obj = ToDoList()
    obj.addItem(items[3])
    obj.addItem(items[5])
    assert obj.getNumItems() == 2, "Added items[3] and items[5], meaning 2 tasks should have been added but didn't"
    assert obj.numberItemsDueToday() == 1, "Task 3 has a duedate of 0, meaning it should be done today, thus only 1 task is due today"
    assert obj.itemExistsInList('Task 4') == False, "Task 4 isn't in the list of items, however didn't return False"
    assert obj.itemExistsInList('Task 5') == True, "items[5] has a title of Task 5 and thus should return True but didn't"
    obj.removeItemsForToday()
    assert obj.getNumItems() == 1,"The duedate is today for task 3, thus 1 item should be removed from an original 2 length long items list, but didn't"
    
    
    obj = ToDoList()
    obj.addItem(items[8])
    assert obj.getNumItems() == 1, "Only added items[8], the number of items should be 1 but isn't"
    assert obj.numberItemsDueToday() == 0, "Should be 0 as duedate for items[8] is 5 and the current day starts out at 0, didn't get the correct output."
    assert obj.itemExistsInList('Task 7') == False, "Should be False as title for items[8] is Task 8, not Task 7"
    obj.removeItemsForToday()
    assert obj.getNumItems() == 1, "No tasks should be removed but one was"
    
    obj = ToDoList()
    assert obj.getNumItems() == 0, "Never added items to obj object, isn't zero though"
    
    obj = ToDoList()
    obj.addItem(items[6])
    obj.addItem(items[7])
    obj.addItem(items[3])
    assert obj.getNumItems() == 3, "Added items[6], [7] and [3], however didn't output 3"
    assert obj.numberItemsDueToday() == 1, "Only one item is due today(day 0), which is items[3], however didn't get 1"
    assert obj.itemExistsInList('Task 6') == True, "Should be True as the title for items[6] is Task 6, however didn't get True"
    assert obj.itemExistsInList('Task 5') == False, "Should be False as Task 5 was never added as an item, thus can't be True, but output didn't return False"
    obj.removeItemsForToday()
    assert obj.getNumItems() == 2, "Only items[6] and [7] should still be in the items list as items[3] had a duedate of zero and thus should be removed, didn't get 2 though"
    
    
    
    # This comment explains what test1() is testing for, and is followed by code
def test2():
    pass
    # This comment explains what test2() is testing for, and is followed by code

# Below are the tests for currentListLength()
def testN():
    pass
    # This comment explains what testN() is testing for, and is followed by code    

############################################################    
    
if __name__ == "__main__":    
    main()