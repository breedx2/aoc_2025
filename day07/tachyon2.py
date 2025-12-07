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

def clone_board(board):
    result = list()
    for row in board:
        result.append(list(row))
    return result

"""
walks the board starting at row_num, until it hits
a splitter. when it does, it puts one or more new 
boards into the timelines. 
"""
def walk_board(timelines, board, row_num):
    # print_board(board, row_num)
    if row_num >= len(board): # spent
        return True
    row = board[row_num]
    for j,ch in enumerate(row):
        above = board[row_num-1][j]
        match ch:
            case '^':
                if above == '|': # beam entering splitter
                    if j > 0 and board[row_num][j-1] == '.':
                        new_board = clone_board(board)
                        new_board[row_num][j-1] = '|' # left timeline
                        timelines.append([new_board, row_num+1])
                    if j < len(row) - 1 and board[row_num][j+1] == '.':
                        new_board = clone_board(board)
                        new_board[row_num][j+1] = '|' # right timeline
                        timelines.append([new_board, row_num+1])
                    return False
            case '.':
                board[row_num][j] = '|' if above == 'S' or above == '|' else '.'
    timelines.append([board, row_num+1])
    return False


timelines = list([[board, 1]])
timeline_ct = 0
while len(timelines) > 0:
    board, row_num = timelines.pop(0)
    if walk_board(timelines, board, row_num):
        timeline_ct = timeline_ct + 1
    print(" timelines size {0}".format(len(timelines)))

print(timeline_ct)
