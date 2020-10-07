# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 14:43:03 2018

@author: LU WANG
"""

'''
Game of life
author: Pleiades
'''

import os
import random

width = 60
height = 60
screen = []


def Init():
    for i in range(height):
        line = []
        for j in range(width):
            if random.random() > 0.8:
                line.append('#')
            else:
                line.append(' ')
        screen.append(line)


def PrintScreen():
    for i in range(height):
        for j in range(width):
            print(screen[i][j] + ' ', end='')
        print()


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


def Start():
    os.system("cls")
    print('== Game of Life ==')
    print('Press any key...')
    input()
    os.system("cls")
    Init()
    PrintScreen()
    c = input()
    while c!= 'q':
        os.system("cls")
        Update()
        PrintScreen()   
        c = input()
    print('End')

Start()