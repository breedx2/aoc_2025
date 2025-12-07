from sys import stdin
import re

board  =  list()
for line in stdin:
    board.append(list(line.rstrip('\n')))

def print_board(board, r):
    for i,row in enumerate(board):
        suf = " <--" if r == i else ""
        print("{0}{1}".format(''.join(row), suf))
    print('-'*len(board[0]))

split_ct = 0
for i,row in enumerate(board):
    if i == 0:
        continue
    new_row = list(row)
    for j,ch in enumerate(row):
        above = board[i-1][j]
        match ch:
            case '^':
                if above == '|': # beam entering splitter
                    split_ct = split_ct + 1
                    if j > 0 and board[i][j-1] == '.':
                        new_row[j-1] = '|'
                    print("cond {0} and {1}".format(j < len(row) - 1, board[i][j+1] == '.'))
                    if j < len(row) - 1 and board[i][j+1] == '.':
                        new_row[j+1] = '|'
                        board[i][j+1] = '|'
                        print("    soon {0}".format(new_row))
            case '.':
                new_row[j] = '|' if above == 'S' or above == '|' else '.'
            case '|':
                pass
                
    print("new row: {0}".format(new_row))
    board[i] = new_row
    print_board(board, i)

    print("splits: {0}".format(split_ct))