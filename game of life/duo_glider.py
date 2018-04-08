# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 16:03:34 2018

@author: LU WANG
"""

'''
Game of life
author: Pleiades
'''

import os

width = 30
height = 30
screen = []


def Init():
    for i in range(height):
        line = []
        for j in range(width):
            line.append(' ')
        screen.append(line)
    screen[10][10]='#'
    screen[9][11]='#'
    screen[11][12]='#'
    screen[10][12]='#'
    screen[9][12]='#'
    screen[10][15]='#'
    screen[9][16]='#'
    screen[11][17]='#'
    screen[10][17]='#'
    screen[9][17]='#'



def PrintScreen():
    for i in range(height):
        for j in range(width):
            print(screen[i][j] + ' ', end='')
        print('|')


def TryGetCell(i, j):
    i = i % height
    j = j % width
    return screen[i][j]


def GetNearbyCellsCount(i, j):
    nearby = []
    nearby.append(TryGetCell(i - 1, j - 1))
    nearby.append(TryGetCell(i - 1, j))
    nearby.append(TryGetCell(i - 1, j + 1))
    nearby.append(TryGetCell(i, j - 1))
    nearby.append(TryGetCell(i, j + 1))
    nearby.append(TryGetCell(i + 1, j - 1))
    nearby.append(TryGetCell(i + 1, j))
    nearby.append(TryGetCell(i + 1, j + 1))
    num = 0
    for x in nearby:
        if x == '#':
            num = num + 1
    return num


def Update():
    global screen
    newScreen = []
    for i in range(height):
        line = []
        for j in range(width):
            line.append(' ')
        newScreen.append(line)
    for i in range(height):
        for j in range(width):
            count = GetNearbyCellsCount(i, j)
            if count == 3:
                newScreen[i][j] = '#'
            elif count < 2 or count > 3:
                newScreen[i][j] = ' '
            else:
                newScreen[i][j] = screen[i][j]    
    screen = newScreen

def Loop():
    Update()
    PrintScreen()


def Start():
    os.system("clear")
    print('== Game of Life ==')
    print('Author: Pleiades')
    print('Press any key...')
    input()
    os.system("clear")
    Init()
    PrintScreen()
    c = input()
    while c != 'q':
        os.system("clear")
        Loop()
        c = input()
    print('End')

Start()