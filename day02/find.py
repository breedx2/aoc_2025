from sys import stdin

sum = 0
line = stdin.readline()
for id_range in line.split(','):
    [lo,hi] = map(int, id_range.split('-'))
    for num in range(lo,hi+1):
        ns = str(num)
        lns = len(ns)
        if lns % 2 == 0:
            first_half = ns[:int(lns/2)]
            last_half = ns[int(lns/2):]
            if first_half == last_half:
                print(ns)
                sum = sum + num
print("------------")
print(sum)