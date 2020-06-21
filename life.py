#!/usr/bin/python

import random
import os
import time


def dead_state(w, h):
    board = [[0 for i in range(w)] for j in range(h)]
    return board


def random_state(w, h):
    threshold = 0.5
    board = [[0 if random.random() > threshold else 1 for i in range(w)] for j in range(h)]
    return board


def render(board):
    for row in board:
        for cell in row:
            if cell == 1:
                print("\033[46m \033[0m", end='')
            else:
                print("\033[44m \033[0m", end='');
        print();


def new_board_state(board):
    w = len(board[0])
    h = len(board)
    new_board = dead_state(w, h)

    for i in range(h):
        for j in range(w):
            neighbours = []
            # conditions for edge cells
            if i-1 >= 0 and j-1 >= 0:
                neighbours.append(board[i-1][j-1])
            if i-1 >= 0:
                neighbours.append(board[i-1][j])
            if i-1 >= 0 and j+1 < w:
                neighbours.append(board[i-1][j+1])
            if j+1 < w:
                neighbours.append(board[i][j+1])
            if i+1 < h and j+1 < w:
                neighbours.append(board[i+1][j+1])
            if i+1 < h:
                neighbours.append(board[i+1][j])
            if i+1 < h and j-1 >= 0:
                neighbours.append(board[i+1][j-1])
            if j-1 >= 0:
                neighbours.append(board[i][j-1])

            cell_state = board[i][j]
            living = neighbours.count(1)

            if cell_state == 1:
                if living < 2:
                    cell_state = 0
                elif living > 3:
                    cell_state = 0
                else:
                    cell_state = 1
            elif cell_state == 0:
                if living == 3:
                    cell_state = 1
                else:
                    cell_state = 0

            new_board[i][j] = cell_state

    return new_board


def print_raw(board):
    for row in board:
        for cell in row:
            print(cell, end = ' ')
        print()


def main():
    board = random_state(40, 20)
    render(board)
    while True:
        os.system("clear")
        new_board = new_board_state(board)
        render(new_board)
        board = new_board
        time.sleep(0.7)


if __name__ == '__main__':
    main()
