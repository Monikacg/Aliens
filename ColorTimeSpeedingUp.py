import random
import os
from math import *
import sys
from termcolor import colored,cprint
import colorama
import msvcrt as ms
import time

width = 20
height = 20
topScore = 0

colorama.init()
clear = lambda: os.system('cls')

def makeBoard(board):
    x = colored('.', 'grey')
    for i in range(width):
        board.append([])
    for i in range(height):
        for j in range(width):
            board[i].append(x)
            if j == width-1:
                board[i].append('|')

def printBoard(board,round,score):
    clear()
    print('TOP SCORE ', topScore)
    print('ROUND ', round)
    print('SCORE ', score)
    for i in board:
        print('|',end='')
        print(*i)
    print('')

def enemies(board):
    a = True
    while a:
        e = random.randint(0,width-1)
        if board[0][e] == colored('#','green'):
            pass
        else:
            board[0][e] = colored('#','green')
            a = False

def player(board):
    board[width-1][0] = colored('o','magenta')

def initiateGame(theBoard):
    makeBoard(theBoard)
    enemies(theBoard)
    player(theBoard)
    printBoard(theBoard,1,0)

def movePlayer(board, i):
    if i == b'a' or i == b'd':
        if i == b'a' and board[width-1][0] == colored('o','magenta'):
            pass
        elif i == b'd' and board[width-1][height-1] == colored('o','magenta'):
            pass
        else:
            for j in range(0,width):
                if board[width-1][j] == colored('o','magenta'):
                    if i == b'a':
                        board[width-1][j] = colored('.', 'grey')
                        board[width-1][j-1] = colored('o','magenta')
                    elif i == b'd':
                        board[width-1][j] = colored('.', 'grey')
                        board[width-1][j+1] = colored('o','magenta')
                        break

def moveEnemies(board, round, score):
    for i in range(width-1,-1,-1):
        for j in range(height-1,-1,-1):
            if board[i][j] == colored('#','green'):
                if i == height-1:
                    board[i][j] = colored('.','grey')
                    score += 1
                elif board[i+1][j] == colored('o','magenta'):
                    printBoard(board, round, score)
                    cprint('YOU LOST!','red')
                    return False, score
                else:
                    board[i][j] = colored('.','grey')
                    board[i+1][j] = colored('#','green')
    return True, score

def moreEnemies(board, round):
    c = random.randint(0,100) + round
    d = int(c/50)
    for i in range(d):
        enemies(board)

def newRound(turn,round):
    if turn % 10 == 0:
        round += 1
    return round

def game(theBoard):
    round = 1
    score = 0
    turn = 1
    play = True
    sleepTime = 1
    while play:
        time.sleep(sleepTime)
        if ms.kbhit():
            i = ms.getch()
            movePlayer(theBoard,i)
        play, score = moveEnemies(theBoard, round, score)
        moreEnemies(theBoard, round)
        turn += 1
        round = newRound(turn,round)
        sleepTime = sleepTime - 0.001
        if sleepTime < 0.1:
            sleepTime = 0.1
        if play:
            printBoard(theBoard, round, score)
    global topScore
    if score > topScore:
        topScore = score
        text = colored('NEW TOP SCORE! FINAL SCORE: ','green')
        print(text, score)
    else:
        print('FINAL SCORE: ', score)

def setHnW():
    f = input('Set width: '), input('Set height: ')
    if (f[0].isdigit() and f[1].isdigit()):
        f = int(f[0]),int(f[1])
        if f[0] > 20:
            width = 20
        else:
            width = f[0]
        if f[1] > 20:
            height = 20
        else:
            height = f[1]
    else:
        width = 20
        height = 20
    return width,height

def main():
    width,height = setHnW()
    topScore = 0
    while True:
        theBoard = []
        initiateGame(theBoard)
        game(theBoard)
        a = input('')

main()
