# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 11:25:02 2022

@author: gabel
"""

def createTable(phrase, phrase_2):
    
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
    
        
    
    
    #Calling the functions in order to get a proper phrase for phrase
    phrase = remove(phrase)
    phrase = lowercase(phrase)
    phrase = puncation(phrase)
    phrase = removeNumbers(phrase)
    print(phrase)
    
    phrase_2 = remove(phrase_2)
    phrase_2 = lowercase(phrase_2)
    phrase_2 = puncation(phrase_2)
    phrase_2 = removeNumbers(phrase_2)
    
    #Create a 5x5 matrix of the alphabet with q removed
    plaintext_cipher_1 = []
    plaintext_cipher_2 =[]
    alphabet = []
    new_string = ''
    
    leftover = []
    for i in range(97, 123):
        if i == 113:
            pass
        else:
            alphabet.append(chr(i))
            
    k = 5
    l = 1
    for i in range(len(alphabet) // 5):
        first_list = []
        for g in range(l):
            data = alphabet[k-5:k]
            for values in data:
                first_list.append(values)
                
            k += 5
            plaintext_cipher_1.append(first_list)
            
    
    k = 5
    l = 1
    for i in range(len(alphabet) // 5):
        first_list = []
        for g in range(l):
            data = alphabet[k-5:k]
            for values in data:
                first_list.append(values)
                
            k += 5
            plaintext_cipher_2.append(first_list)
            
    for i in range(len(plaintext_cipher_1)):
        print(plaintext_cipher_1[i])
        
    
    return plaintext_cipher_1,  plaintext_cipher_2

#################################################################################

def keywordCipher(word1, word2):
    
    #Removes the puncation
    def puncation(string):
        new_string = ''
        puncation = ['.', '!', ',', '?']
        for i in range(len(string)):
            if string[i] in puncation:
                pass
            else:
                new_string += string[i]
                
        return new_string
    
    #Gets the lower case letters
    def lowercase(string):
        return string.lower()
    
    #Removes any strings attached to a word
    def removeSpaces(string):
        return string.replace(" ", "")
    
    def alphabet():
        alphabet = []
        for i in range(97, 123):
            if i == 113:
                pass
            else:
                alphabet.append(chr(i))
        return alphabet
                
    
    word1 = puncation(word1)
    word1 = lowercase(word1)
    word1 = removeSpaces(word1)
    
    word2 = puncation(word2)
    word2 = lowercase(word2)
    word2 = removeSpaces(word2)
    
    def createMatrix(string):
        #Calling the alphabet function and setting to a variable
        alphabets = alphabet()
        
        #Creates a new_string, adds the word to a new_string and then checks the alphabet to check and make sure
        #no duplicates enter the new_string and then creates a 5x5 matrix to used for transposing and encrypting values.
        new_string = ''
        for i in range(len(string)):
            if string[i] not in new_string:
                new_string += string[i]
            else:
                pass
            
        for i in range(len(alphabets)):
            if alphabets[i] not in new_string:
                new_string += alphabets[i]
            else:
                pass
            
        
        #print(new_string)
            
        #Time to create the matrix now
        list_lists = []
        k = 5
        l = 1
        for row in range(len(new_string) // 5):
            first_list = []
            for value in range(l):
                data = new_string[k-5:k]
                for values in data:
                    first_list.append(values)
            
            k += 5
            list_lists.append(first_list)
            
            
        return list_lists
    
    #Calling word1 and word2 through the createMatrix function and returning those
    word1 = createMatrix(word1)
    word2 = createMatrix(word2)
    
    return word1, word2
        

def plaintext(plaintext):
    
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


def fourSquaresRule(pair, plaintext_cipher_1, plaintext_cipher_2, word1, word2):
    coors1 = []
    coors2 = []
    new_string = ''
    for i in range(len(pair)-1):
        # first_letter = pair[i]
        # second_letter = pair[i+1]
        
        for row in range(len(plaintext_cipher_1)):
            for letter in range(len(plaintext_cipher_1[row])):
                
                if str(plaintext_cipher_1[row][letter]) == str(pair[i]):
                    print('Check')
                    
                    
                    coors1.append(row)
                    coors1.append(letter)
                    
                    
        for row in range(len(plaintext_cipher_2)):
            for letter in range(len(plaintext_cipher_2[row])):
                
                if str(plaintext_cipher_2[row][letter]) == str(pair[i+1]):
                    print('check')
                    
                    coors2.append(row)
                    coors2.append(letter)
                    
    
    for i in range(len(coors1)):
    
        for j in range(len(coors2)):
            
            for row in range(len(word1)):
                row = coors1[0]
                for value in range(len(word1[row])):
                    value = int(coors2[1])
                    
                    encrypted_letter = word1[row][value]
                    
                    new_string += encrypted_letter
            
            for row in range(len(word2)):
                row = coors2[0]
                for value in range(len(word2[row])):
                    value = int(coors1[1])
                    
                    second_letter = word2[row][value]
                    
                    new_string += second_letter
            
    return new_string
                    
            
            
    
word1, word2 = createTable('keyword', 'phrase')
plaintext_cipher_1, plaintext_cipher_2 = keywordCipher('gabe', 'dell')
print(plaintext('HELLO WORLD'))
print(fourSquaresRule('he', plaintext_cipher_1, plaintext_cipher_2, word1, word2))