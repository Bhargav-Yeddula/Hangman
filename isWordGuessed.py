# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 09:41:54 2018

@author: Admin
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
#    secretWord = 'apple' 
#    lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    cnt = 0
    for letr in secretWord:
#        print(letr)
        if letr in lettersGuessed:
            cnt+=1
    if cnt == len(secretWord):
        return True
    else:
        return False
