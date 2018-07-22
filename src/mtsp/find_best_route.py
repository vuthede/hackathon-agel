from galogic import *
import matplotlib.pyplot as plt
import sys

points = [(10.775979, 106.647416), (10.778877, 106.645034), (10.778998, 106.646461), (10.778280, 106.647274),
          (10.778584, 106.649881), (10.779987, 106.650601), (10.779507, 106.649450), (10.779073, 106.650368)]

list_dustbin = []
list_point_had_search = []
first_point = 0
num_of_best_points = 3
best_distance = sys.maxsize
best_route = []

def find_best_points(list_dustbin, list_point_had_search, num_of_best_points):
    dist = []
    point = list_dustbin[list_point_had_search[-1]]
    result = []
    for i in range(len(list_dustbin)):
        if i not in list_point_had_search:
            dist.append((i, point.distanceHaversineTo(list_dustbin[i])))
    print(dist)
    dist.sort(key=lambda x: x[1], reverse=False)
    print(dist)
    for i in range(min(num_of_best_points, len(dist))):
        result.append(dist[i])
    return result

def dfs_iterative(list_dustbin, first_point, num_of_best_points):
    stack, path = [list_dustbin[first_point]], []
    num_of_node = len(list_dustbin)
    best_distance = sys.maxsize
    best_route = []

    while stack:
        vertex = stack.pop()
        if vertex[0] in path:
            continue
        path.append(vertex)
        neighbors = find_best_points(list_dustbin, path, num_of_best_points)
        for neighbor in neighbors:
            stack.append(neighbor)
        if (num_of_node == len(path)):
            total_dist = sum([p[1] for p in path])
            if total_dist < best_distance:
                best_distance = total_dist
                best_route = path.copy()
    return path

for point in points:
    list_dustbin.append(Dustbin(point[0], point[1]))

list_point_had_search.append(first_point)
best_for_first_point = find_best_points(list_dustbin, list_point_had_search, num_of_best_points)

for point in best_for_first_point:
    while True:
        

