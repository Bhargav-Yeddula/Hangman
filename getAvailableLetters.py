# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 12:44:08 2018

@author: Admin
"""
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alpa = string.ascii_lowercase
    #print(alpa)
    for letr in lettersGuessed:
        if letr in alpa:
            alpa = alpa.replace(letr, '')
    return alpa
