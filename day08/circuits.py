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
NUM=1000
for i in range(0,NUM):
    combo = sorted_distances.pop(0)
    sorted_distances.pop(0)
    p1 = combo[0]
    p2 = combo[1]
    print('----------------------------')
    print("p1 = {0} p2 = {1}".format(p1, p2))
    print("\n".join(list(map(str, circuits))))

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

print('-------------------------')
print("\n".join(list(map(str, circuits))))
result = 1
sc = sorted(circuits, key = lambda x: len(x), reverse = True)
for c in sc[0:3]:
    print("len => {0}".format(len(c)))
    result = result * len(c)

print("result => {0}".format(result))

# print(points)

# points_sx = sorted(points, key = lambda pt: pt[0])
# points_sy = sorted(points, key = lambda pt: pt[1])
# points_sz = sorted(points, key = lambda pt: pt[2])

# connections = dict()
# circuits = []

# def connect(p1, p2):
#     if p1 in connections:
#         if p2 in connections[p1]:
#             return False # already connected
#         connections[p1].append(p2)
#     else:
#         connections[p1] = [p2]
#     if p2 in connections:
#         connections[p2].append(p1)
#     else:
#         connections[p2] = [p1]
    
#     return True

# def closest(pt):
#     # definitely not sure if this is always valid. There could
#     # and probably will be multiple "neighbors" in one dimension
#     # that are the same distance in that single dimension, in which 
#     # case we should add them all to the candidates, but we're not 
#     # there yet...
#     candidates = set() # might be made better 
#     def add_nearby(sorted_list, pt):
#         # print(pt)
#         # print(sorted_list)
#         ix = sorted_list.index(pt)
#         if ix > 0:
#             n = sorted_list[ix-1]
#             dist = distance(pt, n)
#             candidates.add((n, dist))
#         if ix < len(sorted_list)-1:
#             n = sorted_list[ix+1]
#             dist = distance(pt, n)
#             candidates.add((n, dist))
#     add_nearby(points_sx, pt)
#     add_nearby(points_sy, pt)
#     add_nearby(points_sz, pt)
#     print("pt = {0} candidates: {1}".format(pt, candidates))
#     result = min(candidates, key = lambda x: x[1])
#     print(result)
#     return result

# each_nearest = list(map(lambda pt: [pt, closest(pt)], points))
# print(each_nearest)

# near = sorted(each_nearest, key = lambda x: x[1][1])
# print("\n".join(map(str, near)))
# print()
# print("nearest: {0}".format(near[0]))

# p1 = near[0][0]
# p2 = near[1][0]
# connect(p1, p2)
