#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:39:18 2020
@author: Shivakumar
Version: 0.1
"""
from imdb import IMDb
import random

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

print(bcolors.HEADER+
'''
\t~~ RandoMovieTvGen ~~
'''
+ bcolors.ENDC)

#============== Hollywood Movie ===============#

class ChooseMovie(object):
    def __init__(self):
        self.cursor = IMDb()
        self.top250 = self.cursor.get_top250_movies()
        
    def __repr__(self):
        num = int(random.randint(0,249))
        return str(f"{num}: {self.top250[num]}")

#=============== Hollywood TV ================#

class ChooseTV(object):
    def __init__(self):
        self.cursor = IMDb()
        self.top250 = self.cursor.get_top250_tv()
        
    def __repr__(self):
        num = int(random.randint(0,249))
        return str(f"{num}: {self.top250[num]}")

#============== Bollywood Movie ===============#

class ChooseINDmovie(object):
    def __init__(self):
        self.cursor = IMDb()
        self.top250 = self.cursor.get_top250_indian_movies()
        
    def __repr__(self):
        num = int(random.randint(0,249))
        return str(f"{num}: {self.top250[num]}")

#=============== Print Output ================#

if __name__ == '__main__':
    print(bcolors.BLUE + bcolors.BOLD + "Hollywood Movie: " + bcolors.ENDC)
    print(ChooseMovie())
    print(bcolors.BLUE + bcolors.BOLD + "Hollywood TV: " + bcolors.ENDC)
    print(ChooseTV())
    print(bcolors.BLUE + bcolors.BOLD + "Bollywood Movie: " + bcolors.ENDC)
    print(ChooseINDmovie())

print(bcolors.HEADER+
'''
\t    ~~ Enjoy ~~
'''
+ bcolors.ENDC)
