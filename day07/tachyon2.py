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
                        if j > 0 and board[row_num][j-1] == '.':
                            left = clone_board(board)
                            # original_row = list(row)
                            left[row_num][j-1] = '|' # left timeline
                            # print("go left")
                            child_timelines = walk_board(left, row_num+1)
                            timeline_ct = timeline_ct + child_timelines
                        if j < len(row) - 1 and board[row_num][j+1] == '.':
                            right = clone_board(board)
                            right[row_num][j+1] = '|' # right timeline
                            # print("go right")
                            child_timelines = walk_board(right, row_num+1)
                            timeline_ct = timeline_ct + child_timelines
                        # print("genesis returning {0}".format(timeline_ct))
                        return timeline_ct
                case '.':
                    board[row_num][j] = '|' if above == 'S' or above == '|' else '.'
        row_num = row_num + 1
    # timeline_ct = 1
    # print("returning {0}".format(timeline_ct))
    return 1

ct = walk_board(board, 1)
print(ct)

# timelines = list([[board, 1]])
# timeline_ct = 0
# while len(timelines) > 0:
#     board, row_num = timelines.pop(0)
#     if walk_board(timelines, board, row_num):
#         timeline_ct = timeline_ct + 1
#     print(" timelines size {0}".format(len(timelines)))

# print(timeline_ct)
