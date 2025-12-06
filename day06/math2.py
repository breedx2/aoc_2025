from sys import stdin
from functools import reduce

lines  =  list()
for line in stdin:
    lines.append(list(line.rstrip('\n')))

def mult(lizt):
    return reduce(lambda a,b: a*b, lizt)

def get_col(lines, i):
    return list(map(lambda x: x[i], lines))

def to_num(col):
    # print("col {0} o num".format(col))
    chars = list(filter(lambda x: x != ' ', col[:-1]))
    return int("".join(chars))

op_totals = list()
num_stack = list()
for i in range(len(lines[0])-1, -1, -1):
    col = get_col(lines, i)
    if all(map(lambda x: x == ' ', col)): # blank column
        num_stack = list()
        continue
    n = to_num(col)
    print(n)
    num_stack.append(n)
    if col[-1] != ' ':
        print("num_stack = {0}".format(num_stack))
        op = sum if col[-1] == '+' else mult
        op_totals.append(op(num_stack))

# print(op_totals)
print("------------------")
print(sum(op_totals))