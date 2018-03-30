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

width = 100
height = 1
screen = []


def Init():
    for i in range(height):
        line = []
        for j in range(width):
            line.append(' ')
        screen.append(line)
    screen[0][50]='#'



def PrintScreen():
    for i in range(len(screen)):
        for j in range(width):
            print(screen[i][j] + ' ', end='')
        print('|')


def Update():
    global screen
    s = len(screen)
    line = []
    for j in range(width):
        line.append(' ')
    screen.append(line)
    for j in range(width-1):
        if screen[s-1][j-1]=='#' and screen[s-1][j]=='#' and screen[s-1][j+1]=='#':
            screen[s][j] = ' '
        elif screen[s-1][j-1]=='#' and screen[s-1][j]=='#' and screen[s-1][j+1]==' ':
            screen[s][j] = ' '
        elif screen[s-1][j-1]=='#' and screen[s-1][j]==' ' and screen[s-1][j+1]=='#':
            screen[s][j] = ' '
        elif screen[s-1][j-1]=='#' and screen[s-1][j]==' ' and screen[s-1][j+1]==' ':
            screen[s][j] = '#'
        elif screen[s-1][j-1]==' ' and screen[s-1][j]=='#' and screen[s-1][j+1]=='#':
            screen[s][j] = '#'
        elif screen[s-1][j-1]==' ' and screen[s-1][j]=='#' and screen[s-1][j+1]==' ':
            screen[s][j] = '#'
        elif screen[s-1][j-1]==' ' and screen[s-1][j]==' ' and screen[s-1][j+1]=='#':
            screen[s][j] = '#'
        elif screen[s-1][j-1]==' ' and screen[s-1][j]==' ' and screen[s-1][j+1]==' ':
            screen[s][j] = ' '

def Loop():
    Update()
    PrintScreen()


def Start():
    os.system("clear")
    print('== Game of Life ==')
    print('Author: Pleiades')
    print('Press any key...')
    input()
    os.system("cls")
    Init()
    PrintScreen()
    c = input()
    while c != 'q':
        os.system("clear")
        Loop()
        c = input()
    print('End')



Start()