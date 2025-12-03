from sys import stdin

cache = dict()

def joltage(bank, num, ind = ''):
    key = bank + "+" + str(num)
    if key in cache:
        return cache[key]
    if num == 0 or num > len(bank):
        return ""
    if num == len(bank):
        return bank
    result = bank[:num]
    for i in range(0,len(bank)):
        first = bank[i]
        rest = joltage(bank[i+1:], num-1, ind + " ")
        t = first + rest
        if int(t) > int(result):
            result = t

    cache[key] = result
    return result

total = 0
for bank in stdin:
    j = joltage(bank.strip(), 12)
    print(j)
    total = total + int(j)

print("cache size ended up being {0}".format(len(cache)))
print('--------')
print(total)