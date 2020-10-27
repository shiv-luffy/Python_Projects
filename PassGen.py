#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 08:45:51 2020
@author: Shivakumar
Version: 0.1
"""

## class print output in colour##
class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

## Imports ##
from random import choice, shuffle
from string import ascii_letters as letters, digits, punctuation

print(bcolors.HEADER+
'''
\t~~ PasswordGenerator ~~
'''
+ bcolors.ENDC)

## User inputs ##

password_length = int(input("Enter a length for your Password below:\n"))

## Generate a sequence list ##

character_seq = [choice(letters + digits + punctuation) for i in range(password_length)]

## Shuffle the sequence ##

shuffle(character_seq)

## join the sequence into string ##

pass_gen = "".join(character_seq)

## output ##

print(bcolors.BLUE + "Strong Password generated!\n"+ bcolors.ENDC)
print(bcolors.YELLOW + bcolors.BOLD + f"Your Password is {pass_gen} \n"+ bcolors.ENDC)
