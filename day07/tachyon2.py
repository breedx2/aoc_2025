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

cache = dict()

"""
walks the board starting at row_num, until it hits
a splitter. when it does, it recurses with the
1 or 2 new timelines. returns the total number of timelines
encountered.
"""
def walk_board(board, row_num):
    # print_board(board, row_num)
    while row_num < len(board):
        row = board[row_num]
        for j,ch in enumerate(row):
            above = board[row_num-1][j]
            match ch:
                case '^':
                    if above == '|': # beam entering splitter
                        timeline_ct = 0
                        left = clone_board(board)
                        left[row_num][j-1] = '|' # left timeline
                        key = "".join(left[row_num])
                        if key in cache: # already seen this subtree
                            child_timelines = cache[key]
                        else:
                            child_timelines = walk_board(left, row_num+1)
                            cache[key] = child_timelines
                        timeline_ct = timeline_ct + child_timelines

                        right = clone_board(board)
                        right[row_num][j+1] = '|' # right timeline
                        key = "".join(right[row_num])
                        if key in cache:
                            child_timelines = cache[key]
                        else:
                            child_timelines = walk_board(right, row_num+1)
                            cache[key] = child_timelines
                        timeline_ct = timeline_ct + child_timelines
                        return timeline_ct
                case '.':
                    board[row_num][j] = '|' if above == 'S' or above == '|' else '.'
        row_num = row_num + 1
    return 1

ct = walk_board(board, 1)
print("cache size: {0}".format(len(cache)))
print("answer: {0}".format(ct))