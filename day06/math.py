from sys import stdin
import re

nums  =  list()
ops = list()
for line in stdin:
    parts = re.split(r'\s+'  , line.strip())
    if parts[0] == "+" or parts[0] == "*":
        ops = ops + parts
    else:
        nums.append(list(map(int, parts)))

print(ops)
totals = list(map(lambda x: 0 if x == "+" else 1, ops))
print(totals)
for i,op in enumerate(ops):
    for row in nums:
        if op == "+":
            totals[i] = totals[i] + row[i]
        else:
            totals[i] = totals[i] * row[i]

print(totals)
final = sum(totals)
print(final)