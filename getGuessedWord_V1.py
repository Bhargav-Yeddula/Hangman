# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 12:54:05 2018

@author: Admin
"""

def getGuessedWord(secretWord, lettersGuessed):
     '''
     secretWord: string, the word the user is guessing
     lettersGuessed: list, what letters have been guessed so far
     returns: string, comprised of letters and underscores that represents
       what letters in secretWord have been guessed so far.
     '''
     
     ans = secretWord
     for letr in secretWord:
#         print(letr)
         if not letr in lettersGuessed:
             ans = ans.replace(letr,' _ ')
#             print(ans)
     return ans