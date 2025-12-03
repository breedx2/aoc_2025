from sys import stdin

def joltage(bank):
    result = int(bank[:2])
    for i in range(0,len(bank)):
        for j in range(i+1,len(bank)):
            value = int(bank[i] + bank[j])
            if value > result:
                result = value
    return result

total = 0
for bank in stdin:
    j = joltage(bank)
    print(j)
    total = total + j

print('--------')
print(total)