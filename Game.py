import random
import os
from math import *

width = 10
height = 10
topScore = 0

clear = lambda: os.system('cls')

def makeBoard(board):
    x = '*'
    for i in range(width):
        board.append([])
    for i in range(height):
        for j in range(width):
            board[i].append(x)

def printBoard(board,round,score):
    clear()
    print('TOP SCORE ', topScore)
    print('ROUND ', round)
    print('SCORE ', score)
    for i in board:
        print(*i)
    print('')

def enemies(board):
    a = True
    while a:
        e = random.randint(0,width-1)
        if board[0][e] == '#':
            pass
        else:
            board[0][e] = '#'
            a = False

def player(board):
    board[width-1][0] = 'o'

def initiateGame(theBoard):
    makeBoard(theBoard)
    enemies(theBoard)
    player(theBoard)
    printBoard(theBoard,1,0)

def movePlayer(board, i):
    if i == 'a' or i == 'd':
        if i == 'a' and board[width-1][0] == 'o':
            pass
        elif i == 'd' and board[width-1][height-1] == 'o':
            pass
        else:
            for j in range(0,width):
                if board[width-1][j] == 'o':
                    if i == 'a':
                        board[width-1][j] = '*'
                        board[width-1][j-1] = 'o'
                    elif i == 'd':
                        board[width-1][j] = '*'
                        board[width-1][j+1] = 'o'
                        break

def moveEnemies(board, round, score):
    for i in range(width-1,-1,-1):
        for j in range(height-1,-1,-1):
            if board[i][j] == '#':
                if i == height-1:
                    board[i][j] = '*'
                    score += 1
                elif board[i+1][j] == 'o':
                    printBoard(board, round, score)
                    print('You lost!')
                    return False, score
                else:
                    board[i][j] = '*'
                    board[i+1][j] = '#'
    return True, score

def moreEnemies(board, round):
    c = random.randint(0,100) + round
    if c > 75:
        enemies(board)
        if c > 100:
            enemies(board)
            if c > 125:
                enemies(board)
                if c > 150:
                    enemies(board)
                    if c > 175:
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
    while play:
        i = input('press a for left or d for right: ')
        movePlayer(theBoard,i)
        play, score = moveEnemies(theBoard, round, score)
        moreEnemies(theBoard, round)
        turn += 1
        round = newRound(turn,round)
        if play:
            printBoard(theBoard, round, score)
    global topScore
    if score > topScore:
        topScore = score
        print('NEW TOP SCORE! FINAL SCORE: ', score)
    else:
        print('FINAL SCORE: ', score)

def main():
    while True:
        theBoard = []
        initiateGame(theBoard)
        game(theBoard)
        a = input('')

main()
