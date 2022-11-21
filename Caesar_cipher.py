# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 09:36:08 2022

@author: gabel
"""

def newAlphabet(shift):
    
    alphabet = []
    leftover_alphabet = []
    new_alphabet = []
    string = ''
    encrypted_phrase = ''
    
    user = input('Passphrase to be encrypted: ')
    if shift > 0:
        pass
    else:
        return None
    
    def removeSpaces(user):
        return user.replace(" ", "")
    
    def puncation(string):
        new_string = ''
        puncation = ['.', '!', ',', '?']
        for i in range(len(string)):
            if string[i] in puncation:
                pass
            else:
                new_string += string[i]
                
        return new_string
    
    #Calls helper functions in order to get a proper phrase to deal with later on
    user = removeSpaces(user)
    user = puncation(user)
    
    
    #Creates an uppercase alphabet
    for i in range(65, 91):
        alphabet.append(chr(i))

    
    #Letters that are going to be shifted, appended to leftover alphabet
    for i in range(shift):
        leftover_alphabet.append(alphabet[i])
    
    #Takes the shift and adds any letter from the shift to the end of the alphabet list to an empty string
    for i in range(len(alphabet)-shift):
        string += alphabet[shift + i]

    
    #Takes the first letters from the shift away and adds them to the end of the string
    for i in range(len(leftover_alphabet)):
        string += leftover_alphabet[i]

    
    #Takes the string input and adds to a new encrypted alphabet
    for i in range(len(string)):
        new_alphabet.append(string[i])
    
    
    #Makes it so that the new_alphabet letters correspond to the old alphabet sequence and then from that, if user[k] letter
    # is equal to alphabet letter, then take the same position of j and its letter from the alphabet list that would correspond to it
    #and then add to the encrypted phrase and it is then returned
    for k in range(len(user)):
        for j in range(len(new_alphabet)):
            if user[k] == alphabet[j]:
                encrypted_phrase += new_alphabet[j]
                
                
    return encrypted_phrase
                
    
print(newAlphabet(10))