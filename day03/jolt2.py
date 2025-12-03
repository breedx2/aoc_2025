from sys import stdin

def joltage(bank, num, ind = ''):
    print("{0}bank {1} num {2}".format(ind, bank, num))
    if num == 0 or num > len(bank):
        return ""
    if num == len(bank):
        return bank
    result = bank[:num]
    for i in range(0,len(bank)):
        first = bank[i]
        rest = joltage(bank[i+1:], num-1, ind + " ")
        t = first + rest
        # print("{0}check {1} vs {2}".format(ind, result, int(t)))
        if int(t) > int(result):
            result = t

    print("{0}bank {1} num {2} yields {3}".format(ind, bank, num, result))
    return result

total = 0
for bank in stdin:
    j = joltage(bank.strip(), 12)
    print(j)
    total = total + int(j)

print('--------')
print(total)