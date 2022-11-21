# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:59:57 2020

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Gabriel Dell
"""

from string import ascii_lowercase

def createTable(phrase):
    '''
    Given an input string, create a lowercase playfair table.  The
    table should include no spaces, no punctuation, no numbers, and 
    no Qs -- just the letters [a-p]+[r-z] in some order.  Note that 
    the input phrase may contain uppercase characters which should 
    be converted to lowercase.
    
    Input:   string:         a passphrase
    Output:  list of lists:  a ciphertable
    '''
    #Removes spaces
    def remove(string):
        return string.replace(" ", "")
    
    
    
    #Looks for puncation in the phrase and returns out a sentence without puncation
    def puncation(string):
        new_string = ''
        puncation = ['.', '!', ',', '?']
        for i in range(len(string)):
            if string[i] in puncation:
                pass
            else:
                new_string += string[i]
                
        return new_string
    
    #Turns every letter into lowercase
    def lowercase(string):
        return string.lower()
    
    #Removes any numbers in a string using list comphrension
    def removeNumbers(string):
        string = ''.join((element for element in string if not element.isdigit()))
        return string
    
    
    #Calling the functions in order to get a proper phrase
    phrase = remove(phrase)
    phrase = lowercase(phrase)
    phrase = puncation(phrase)
    phrase = removeNumbers(phrase)
    print(phrase)
    
    
    string = ''
    new_string = ''
    list_lists = []

    #This for loop gets every character expect for q in the alphabet and appends to a alphabet list
    alphabet = []
    for i in range(97, 123):
        if i == 113:
            pass
        else:
            alphabet.append(chr(i))
            
    #Removes any 'q' or capital 'q' from the phrase and appends that to an empty string called string        
    for i in range(len(phrase)):
        if phrase[i] == 'q' or phrase[i] == 'Q':
            pass
        else:
            string += phrase[i]
    
    
    
    #If the phrase of the letter is not in the empty string, append it to the string to get a new_string of the phrase
    for i in range(len(string)):
        if string[i] not in new_string:
            new_string += string[i]
        else:
            pass


    #This for loop should provide a way to remove duplicate letters, by checking if they are or arent in the new_string
    for i in range(len(alphabet)):
        #Takes the list and appendes it to a leftOver letter list, essientally all unused letters in the alphabet
        if alphabet[i] not in new_string:
            #leftOver.append(alphabet[i])
            new_string += alphabet[i]
        else:
            pass
    
        
        
    #############################################################
    #Taking the string and splitting it into multiple seperate lists
    k = 5
    l = 1
    for i in range(len(new_string) // 5):
        first_list = []
        for g in range(l):
            #Taking k-5:k because I need the first value and add 5 to that to get a list of 5 values in a list
            data = new_string[k-5:k]
            data.split()
            for values in data:
                first_list.append(values)
            
            k += 5
            list_lists.append(first_list)


    return list_lists


def splitString(plaintext):
    '''
    Splits a string into a list of two-character pairs.  If the string
    has an odd length, append an 'x' as the last character.  As with
    the previous function, the bigrams should contain no spaces, no
    punctuation, no numbers, and no Qs.  Return the list of bigrams,
    each of which should be lowercase.
    
    Input:   string:  plaintext to be encrypted
    Output:  list:    collection of plaintext bigrams
    '''
    
    bigram = []

    # For loop to remove any q's from the phrase
    def lowercase(wordle):
        return wordle.lower()

    #Replacing spaces and closing them
    def remove(spaces):
        return spaces.replace(" ", "")


    def removePuncation(word):
        new_string = ''
        puncation = ['.', '!', ',', '?']
        for i in range(len(word)):
            if word[i] in puncation:
                    pass
            else:
                new_string += word[i]
                    
        return new_string


    plaintext = lowercase(plaintext)
    plaintext = remove(plaintext)
    plaintext = removePuncation(plaintext)

    #Replacing 'q' or 'Q'
    plaintext = plaintext.replace('q', '')
    plaintext = plaintext.replace('Q', '')


    #Taking the plaintext and taking 2 character pairs
    #While loop should keep adding a x until is remainder is 0, meaning even length
    if len(plaintext) % 2 != 0:
        plaintext = plaintext + 'x'

        
    scale = 2
    for i in range(len(plaintext)//2):
        bigram.append(plaintext[scale-2:scale])
        scale += 2
    print(bigram)
           
    return bigram
        

    

def playfairRuleOne(pair):
    '''
    If both letters in the pair are the same, replace the second
    letter with 'x' and return; unless the first letter is also
    'x', in which case replace the second letter with 'z'.
    
    You can assume that any input received by this function will 
    be two characters long and already converted to lowercase.
    
    After this function finishes running, no pair should contain two
    of the same character   
    
    Input:   string:  plaintext bigram
    Output:  string:  potentially modified bigram
    '''
    #Taking the 2 character pair from the bigram list and splitting it
    string = ''
    for i in range(len(pair)-1):
        first_letter = pair[i]
        second_letter = pair[i+1]
        
        #First letter equal to second letter
        if first_letter == second_letter:
            
            #if first letter is x then second letter is z
            if first_letter == 'x':
                second_letter = 'z'
                string += first_letter
                string += second_letter
            else:
                #second letter is x otherwise
                second_letter = 'x'
                string += first_letter
                string += second_letter
        else:
            return pair
        
    return string
    
    
    
    
    

def playfairRuleTwo(pair, list_lists):
    '''
    If the letters in the pair appear in the same row of the table, 
    replace them with the letters to their immediate right respectively
    (wrapping around to the left of a row if a letter in the original
    pair was on the right side of the row).  Return the new pair.
    
    You can assume that the pair input received by this function will 
    be two characters long and already converted to lowercase, and
    that the Playfair Table is valid.
    
    Input:   string:         potentially modified bigram
    Input:   list of lists:  ciphertable
    Output:  string:         potentially modified bigram
    '''
    coors1 = []
    coors2 = [] 
    new_pair = '' 

    #Get the letter from the pair
    
    for letter in range(len(pair)-1):
        
        #Get the list value
        for lists in range(len(list_lists)):
        
            #Get value from those sublist
            for value in range(len(list_lists[lists])):
                
                #Checks if they are on the same row
                if str(list_lists[lists][value]) == str(pair[letter]):
            
                    #Append sublist and values of the letter to coors1
                    coors1.append(lists)
                    coors1.append(value)
                    
                    #If coors1 == 4, meaning end of the sublist, go back to the beginning
                    if coors1[1] == 4:
                        coors1[1] = list_lists[lists][0]
                    else:
                        #Just add one to the value and store that as value in coors1[1]
                        coors1[1] = list_lists[lists][value+1]
                        
                #Do the same exact thing as before for the first letter   
                if str(list_lists[lists][value]) == str(pair[letter+1]):
                    #Append values to coors2
                    coors2.append(lists)
                    coors2.append(value)
                
                
                    if int(coors2[1]) == 4:
                        coors2[1] = list_lists[lists][0]
                        print(coors2[1])
                    else:
                        coors2[1] = list_lists[lists][value+1]
                    
    #If coors[0] and coors[1], meaning they are on the same row, add coor2[1] and coors1[1] to new pair and return else
    # return the normal pair       
    if coors1[0] == coors2[0]:
        new_pair += coors1[1]
        new_pair += coors2[1]
        return new_pair
    else:
        return pair
                    
    


def playfairRuleThree(pair, list_lists):
    '''
    If the letters in the pair appear in the same column of the table, 
    replace them with the letters immediately below respectively
    (wrapping around to the top of a column if a letter in the original
    pair was at the bottom of the column).  Return the new pair.
    
    You can assume that the pair input received by this function will 
    be two characters long and already converted to lowercase, and
    that the Playfair Table is valid.
    
    Input:   string:         potentially modified bigram
    Input:   list of lists:  ciphertable
    Output:  string:         potentially modified bigram
    '''    
    
    #Creating a transposed matrix for the columns
    new_sublist = []
    
    #Creating a list
    transposed = list()
    #Takes the values of the list_lists
    for i in range(len(list_lists[0])):
        #Creates row list
        row = list()
        #Gets sublist
        for new_sublist in list_lists:
            #Appended those sublist values from the columns to row
            row.append(new_sublist[i])
        #Appends to the transposed list
        transposed.append(row)    

    #For easy visualization of transposed list; aribitary 
    for i in range(len(transposed)):
        print(transposed[i])
    # ###########################################################

    coors1 = []
    coors2 = [] 
    new_pair = '' 
    for letter in range(len(pair)-1):
        #first_letter = pair[letter]
        #second_letter = pair[letter+1]  
        
        for lists in range(len(transposed)):
            
            for value in range(len(transposed[lists])):
                
                #Checks if they are on the same row
        
                if str(transposed[lists][value]) == str(pair[letter]):
            
                    coors1.append(lists)
                    coors1.append(value)
                    
                    if coors1[1] == 4:
                        coors1[1] = transposed[lists][0]
                    else:
                        coors1[1] = transposed[lists][value+1]
                    
                if str(transposed[lists][value]) == str(pair[letter+1]):
                    
                    coors2.append(lists)
                    coors2.append(value)
                
                    if int(coors2[1]) == 4:
                        coors2[1] = transposed[lists][0]
                       
                    else:
                        coors2[1] = transposed[lists][value+1]
                
    if coors1[0] == coors2[0]:
        new_pair += coors1[1]
        new_pair += coors2[1]
        return new_pair
    else:
        return pair
    


def playfairRuleFour(pair, list_lists):
    '''
    If the letters are not on the same row and not in the same column, 
    replace them with the letters on the same row respectively but in 
    the other pair of corners of the rectangle defined by the original 
    pair.  The order is important -- the first letter of the ciphertext
    pair is the one that lies on the same row as the first letter of 
    the plaintext pair.
    
    You can assume that the pair input received by this function will 
    be two characters long and already converted to lowercase, and
    that the Playfair Table is valid.  
    
    Input:   string:         potentially modified bigram
    Input:   list of lists:  ciphertable
    Output:  string:         potentially modified bigram
    '''
    new_pair = ''
    first_letter_position = []
    second_letter_position = []
    new_first_position = []
    new_second_position = []
    
    
    #Gets the values of the lists
    for lists in range(len(list_lists)):

        #Gets the values of the sublists, individual values
        for value in range(len(list_lists[lists])):
            
            #Gets pairs and their individual letters
            for letter in range(len(pair)-1):
   
                #If the string of values is equal to first letter in the pair, append to first_letter_position list
                if str(list_lists[lists][value]) == str(pair[letter]):
                    first_letter_position.append(lists)
                    first_letter_position.append(value)
                    
                #If the string of values is equal to the second letter in the pair, append to second_letter_position list
                if str(list_lists[lists][value]) == str(pair[letter+1]):
                    second_letter_position.append(lists)
                    second_letter_position.append(value)
                #Else pass
                else:
                    pass
                
                

    #Taking and swapping the positions
    #Position in first_letter_position and second_letter_position and seeing the values of those.
    for position in range(len(first_letter_position)-1):
        for position in range(len(second_letter_position)-1):
            
            #It is in 2 lists, first and second_letter_position to compare, get the corner values and swap them
            #Take new first letter position and append the second_letter_position first position, or the x value
            new_first_position.append(second_letter_position[position])
            #Takes first_letter position of the y value and appends it and gets a new letter position list
            new_first_position.append(first_letter_position[position+1])
            
            #new_second_position of the second character in the pair, appended first_letter_position's x-value
            new_second_position.append(first_letter_position[position])
            #new_second_postion of the second character in the pair, appended second_letter_position y-value
            new_second_position.append(second_letter_position[position+1])        



    #Gets the list_lists values of the new_second_postition of its lists and its values to get a letter and appendes to new_pair
    new_pair += list_lists[int(new_second_position[0])][int(new_second_position[1])]
    new_pair += list_lists[int(new_first_position[0])][int(new_first_position[1])]
    
    return new_pair
    
    
    

def encrypt(pair, list_lists):
    '''
    Given a character pair, run it through all four rules to yield
    the encrypted version!
    
    Input:   string:         plaintext bigram
    Input:   list of lists:  ciphertable
    Output:  string:         ciphertext bigram
    '''
    
    #Goes through all the rules by calling the previous mutation until it gets to the fourth mutation and then returns that.
    first_mutation = playfairRuleOne(pair)
    second_mutation = playfairRuleTwo(first_mutation, list_lists)
    third_mutation = playfairRuleThree(second_mutation, list_lists)
    fourth_mutation = playfairRuleFour(third_mutation, list_lists)
    
    return fourth_mutation




def joinPairs(pairsList):
    '''
    Given a list of many encrypted pairs, join them all into the 
    final ciphertext string (and return that string)
    
    Input:   list:    collection of ciphertext bigrams
    Output:  string:  ciphertext
    '''
    
    #Takes the pairlist, goes into a loop, takes the pairlist[bigram] and adds to an empty string called ciphertext
    # to get the cipher text
    cipherText = ''
    for bigram in range(len(pairsList)):
        cipherText += pairsList[bigram]
    
    return cipherText




def main():
    '''
    Example main() function; can be commented out when running your
    tests
    '''
    table = createTable("i am entering a pass phrase")
    splitMessage = splitString("this is a test message")
    pairsList = []

    #print(table) # printed for debugging purposes
    
    for pair in splitMessage:
        # Note: encrypt() should call the four rules
        pairsList.append(encrypt(pair, table))
    cipherText = joinPairs(pairsList)    
    
    print(cipherText) #printed as the encrypted output
    #output will be hjntntirnpginprnpm
    # print(playfairRuleTwo('am', table))
    # print(playfairRuleTwo('ed', table))
    # print(playfairRuleThree('ax', table))
    # print(playfairRuleFour('ck', table))
    # print(playfairRuleTwo('ba', table))
    print(playfairRuleTwo('cf', table))
    print(playfairRuleTwo('bk', table))
    #print(playfairRuleTwo('dh', table))
    #print(table)
    test1()
    print('ALL TESTS PASSED')


###############################################################

# Here is where you will write your test case functions
    
# Below are the tests for createTable()
def test1():
    # This comment explains what test1() is testing for, and is followed by code
    
    # CreateTable function
    assert createTable('i am entering a passphrase.') ==  [['i', 'a', 'm', 'e', 'n'], ['t', 'r', 'g', 'p', 's'], ['h', 'b', 'c', 'd', 'f'], ['j', 'k', 'l', 'o', 'u'], ['v', 'w', 'x', 'y', 'z']], "Apparently the phrase, 'i am enter a passphrase', didn't return the proper list"
    # SplitString function
    assert splitString('this is my plaintext') == ["th", "is", "is", "my", "pl", "ai", "nt", "ex", "tx"], "Entering the phrase, 'This is my plaintext', didnt return the proper list, check the function"
    assert splitString('this is my home') == ['th', 'is', 'is', 'my', 'ho', 'me'], "Entering the phrase, 'this is my home', didnt return the proper list, check the function"
    assert splitString('may the force be with you') == ['ma', 'yt', 'he', 'fo', 'rc', 'eb', 'ew', 'it', 'hy', 'ou'], "Entering the famous Star Wars quote didn't return the proper list, check the function"
    assert splitString('I will be back') == ['iw', 'il', 'lb', 'eb', 'ac', 'kx'], "Inputting the Terminator's automated catch phrase, didn't yield the correct list, hasta la vita, back to your function"
    assert splitString('A martini, Shaken, not stirred.') == ['am', 'ar', 'ti', 'ni', 'sh', 'ak', 'en', 'no', 'ts', 'ti', 'rr', 'ed'], "Didn't get the correct output."
    
    #PlayfairRuleOne Function tests
    assert playfairRuleOne('aa') == 'ax', "aa should be ax, as if 2 of the same letters are inputted, the second one should be changed"
    assert playfairRuleOne('xx') == 'xz', "xx should be xz, as the second letter should change to an x if only the first letter isn't an x, in this it is, should change to a z"
    assert playfairRuleOne('ab') == 'ab', "ab shouldn't change, not the same letter"
    assert playfairRuleOne('cx') == 'cx', "cx shouldn't change either, not the same letter"
    
    #playfairRuleTwo Function tests
    assert playfairRuleTwo('am', createTable('i am entering a passphrase.')) == 'me', "Checks the rows and moves them to the right by one based on position, yours didnt"
    assert playfairRuleTwo('pt', createTable('i am entering a passphrase.')) == 'sr', "Same row, didn't get the proper value"
    assert playfairRuleTwo('cf', createTable('i am entering a passphrase.')) == 'dh', "Same row again, didn't get the proper value, check function"
    assert playfairRuleTwo('ed', createTable('i am entering a passphrase.')) == 'ed', "Different rows, thus shouldn't change."
    
    #playfairRuleThree Function tests
    assert playfairRuleThree('th', createTable('i am entering a passphrase.')) == 'hj', "Should be moved one down or to the right if transposed, didnt though"
    assert playfairRuleThree('tv', createTable('i am entering a passphrase.')) == 'hi', "Should be moved one down or to the right if transposed, didnt though, check function"
    assert playfairRuleThree('ax', createTable('i am entering a passphrase.')) == 'ax', "Shouldn't change  as on different columns and rows, should be only on different columns"
    assert playfairRuleThree('pd', createTable('i am entering a passphrase.')) == 'do', "Should change as on different columns, didn't shift or go to the correct positions"
    
    #playfairRuleFour Function tests
    assert playfairRuleFour('as', createTable('i am entering a passphrase.')) == 'nr', "Didn't shift to correct places, possible fangling of the numbers or the postions"
    assert playfairRuleFour('jw', createTable('i am entering a passphrase.')) == 'kv', "Didn't shift properly or returned incorrect pair, check function"
    assert playfairRuleFour('do', createTable('i am entering a passphrase.')) == 'do', "Will not change as the positions though changed are in the same spots as before the switch"
    assert playfairRuleFour('fm', createTable('i am entering a passphrase.')) == 'cn', "fm didn't yield cn for so mix up on the positions or whatever"
    
    #encrypt function
    
    pass

def test2():
    # This comment explains what test2() is testing for, and is followed by code
    pass

# Below are the tests for splitString()
def testN():
    # This comment explains what testN() is testing for, and is followed by code
    pass
    
    


    
###############################################################    
    
if __name__ == "__main__":
    main()        