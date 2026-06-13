#!/usr/bin/env python3
# generate_random_words_broken.py
# ARCHIVED: Trivial + broken.
#
# Generates short random alphanum "words".
# The buildWordStartedWith(letter) function completely ignores its
# parameter and always produces something starting with 'z'.
# No CLI, 2014 demo code.
#
# Originally: messy_area/generateRandomWords.py

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 01:13:54 2014

@author: gl00ten
"""


from random import randrange

group = '0123456789abcdefghijklmnopqrstuvwxy'
wordLen = 4

def buildWord():
    word = ''
    while len(word) <= wordLen:
        word = word + group[randrange( 0,len(group) )]
    return word
    

def buildWordStartedWith(letter):
    word = 'z'
    while len(word) <= wordLen:
        word = word + group[randrange( 0,len(group) )]
    return word


wordList = []

for x in range (0,10):
    wordList.append(buildWord())
    
print(wordList)
