from sys import stdin
import math

def read_points():
    result = list()
    for line in stdin:
        result.append(tuple(map(int, line.rstrip('\n').split(','))))
    return result

def distance(p1, p2):
    d1 = abs(p1[0] - p2[0])
    d2 = abs(p1[1] - p2[1])
    d3 = abs(p1[2] - p2[2])
    return math.sqrt((d1*d1) + (d2*d2) + (d3*d3))

points = read_points()

distances = []
# compute distance between every point to every other point! EEEK!
for p1 in points:
    for p2 in points:
        if p1 != p2:
            distances.append((p1,p2,distance(p1,p2)))

print("distances size: {0}".format(len(distances)))

sorted_distances = sorted(distances, key = lambda x: x[2])
# print("\n".join(map(str, sorted_distances)))

def circuit_index(circuits, pt):
    for i,c in enumerate(circuits):
        if pt in c:
            return i
    return -1

circuits = []
finish = []
while True:
    combo = sorted_distances.pop(0)
    sorted_distances.pop(0)
    p1 = combo[0]
    p2 = combo[1]
    print('----------------------------')
    print("p1 = {0} p2 = {1} (remain = {2}, dist = {3})".format(p1, p2, len(sorted_distances), combo[2]))
    # print("\n".join(list(map(str, circuits))))

    i1 = circuit_index(circuits, p1)
    i2 = circuit_index(circuits, p2)
    if i1 < 0 and i2 < 0: # new circuit
        print("New circuit: {0}<-->{1}".format(p1, p2))
        circuits.append([p1,p2])
    elif i1 >= 0 and i2 >= 0: # join 2 existing circuits!
        print("Join circuits {0} and {1}".format(i1, i2))
        if i1 == i2:
            print("  already joined!")
        else:
            circuits[i1].extend(circuits[i2])
            second = circuits.pop(i2)
    elif i1 >= 0:
        print("Connect {0} to {1} via circuit {2}".format(p2, p1, i1))
        circuits[i1].append(p2)
    elif i2 >= 0:
        print("Connect {0} to {1} via circuit {2}".format(p1, p2, i2))
        circuits[i2].append(p1)

    if len(circuits) == 1 and len(circuits[0]) == len(points):
        print("We finished with {0} and {1}!".format(p1, p2))
        finish.append(p1)
        finish.append(p2)
        break


# print('-------------------------')
# print("\n".join(map(str, sorted_distances)))
print('-------------------------')
print("there are {0} circuits".format(len(circuits)))
if len(circuits) > 1:
    raise "Too many puppies"
result = finish[0][0] * finish[1][0]
print("** result: {0}".format(result))
