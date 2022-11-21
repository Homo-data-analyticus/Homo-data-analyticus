'''
Project 5 - Library - Fall 2021 
Author: Gabriel Dell and gabriel21

The book class is supposed to create instance data from the book title and the book author and then
return a one line sequence of a book object describing the title and author.

I have neither given or received unauthorized assistance on this assignment.
Signed:Gabriel Dell
'''

#Define book class
class Book:
    def __init__(self, title, author):
        #Should store book title and author in instance variables
        self.title = title
        self.author = author
    
    def __str__(self):
        #Should return a string description of 'book by author'
        return self.title + ' by ' + self.author