from sys import stdin

def check_invalid(id, num):
    if len(id) % num != 0:
        return False
    part = id[0:num]
    return id == (part * int(len(id)/num))

def is_invalid(id):
    for num in range(1,int(len(id)/2)+1):
        if check_invalid(id, num):
            return True
    return False

sum = 0
line = stdin.readline()
for id_range in line.split(','):
    [lo,hi] = map(int, id_range.split('-'))
    for num in range(lo,hi+1):
        id = str(num)
        if is_invalid(id):
            print("INVALID: {0}".format(id))
            sum = sum + num

print("------------")
print(sum)