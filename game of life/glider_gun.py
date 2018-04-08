# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 15:35:20 2018

@author: LU WANG
"""

'''
Game of life
author: Pleiades
'''

import os

width = 50
height = 50
screen = []


def Init():
    for i in range(height):
        line = []
        for j in range(width):
            line.append(' ')
        screen.append(line)
    screen[2][26]='#'
    screen[3][24]='#'
    screen[3][26]='#'
    screen[4][14]='#'
    screen[4][15]='#'
    screen[4][22]='#'
    screen[4][23]='#'
    screen[4][36]='#'
    screen[4][37]='#'
    screen[5][13]='#'
    screen[5][17]='#'
    screen[5][22]='#'
    screen[5][23]='#'
    screen[5][36]='#'
    screen[5][37]='#'
    screen[6][2]='#'
    screen[6][3]='#'
    screen[6][12]='#'
    screen[6][18]='#'
    screen[6][22]='#'
    screen[6][23]='#'
    screen[7][2]='#'
    screen[7][3]='#'
    screen[7][12]='#'
    screen[7][16]='#'
    screen[7][18]='#'
    screen[7][19]='#'
    screen[7][24]='#'
    screen[7][26]='#'
    screen[8][12]='#'
    screen[8][18]='#'
    screen[8][26]='#'
    screen[9][13]='#'
    screen[9][17]='#'
    screen[10][14]='#'
    screen[10][15]='#'


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