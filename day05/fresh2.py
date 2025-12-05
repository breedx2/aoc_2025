from sys import stdin

def read_ranges():
    ranges = list()
    for line in stdin:
        if len(line.strip()) == 0:
            return ranges
        range = line.strip().split('-')
        range = list(map(int, range))
        ranges.append(range)
    return ranges

def optimize(ranges):
    s = sorted(ranges, key = lambda x: x[0])
    i = 0
    term = len(s)-1
    while i < term:
        r = s[i]
        n = s[i+1]
        if r[1] >= n[0]:
            print("combine {0} and {1}".format(r, s[i+1]))
            s.pop(i)
            s.pop(i)
            s.insert(i, [r[0], max(r[1], n[1])])
            term = len(s)-1
        else:
            i = i + 1
    return s

original_ranges = read_ranges()
print(original_ranges)

ranges = optimize(original_ranges)
print(ranges)

ct = 0
for r in ranges:
    ct = ct + 1 + (r[1]-r[0])

print("---------")
print(ct)