# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 12:10:36 2018

@author: Admin
"""

def getGuessedWord(secretWord, lettersGuessed):
     '''
     secretWord: string, the word the user is guessing
     lettersGuessed: list, what letters have been guessed so far
     returns: string, comprised of letters and underscores that represents
       what letters in secretWord have been guessed so far.
     '''
     
     inpword = secretWord; cnt =0
     for letr in secretWord:
#         print(letr)
         if not letr in lettersGuessed:
             ans = inpword.replace(letr,' _ ')
             inpword = ans; cnt += 1
#             print(ans)
     if cnt == 0:
         return secretWord
     else:
         return ans
