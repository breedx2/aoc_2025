
#!/usr/bin/env python3

from sys import stdin

ct = 0
pos = 50
for line in stdin:
    mod = 1
    if line[0] == 'L':
        mod = -1
    val = int(line[1:])
    for i in range(0, val):
        pos = pos + mod
        if pos > 99:
            pos = 0
        if pos < 0:
            pos = 99
        if pos == 0:
            ct = ct + 1

print(ct)
    
