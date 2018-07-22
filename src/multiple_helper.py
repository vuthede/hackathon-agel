# Python program to print all paths from a source to destination.
  
from collections import defaultdict
from src.galogic import *
import matplotlib.pyplot as plt
import sys
  
#This class represents a directed graph 
# using adjacency list representation
class Graph:
  
    def __init__(self, list_dustbin, num_of_best_points, first_point):
        #No. of vertices
        self.best_distance = sys.maxsize
        self.best_route = []
        self.list_dustbin = list_dustbin
        self.num_of_best_points = num_of_best_points
        self.first_point = first_point
        self.best_path = []
        
    def print_best_route(self):
        self.printAllPaths()
        print(self.best_distance)
        print(self.best_path)

    def find_best_points(self, list_point_had_search):
        """list_point_had_search is a list index of points have searched, return value is a list tupe of (index, and distance)"""
        dist = []
        point = self.list_dustbin[list_point_had_search[-1]]
        result = []
        for i in range(len(self.list_dustbin)):
            if i not in list_point_had_search:
                dist.append((i, point.distanceHaversineTo(self.list_dustbin[i])))
        dist.sort(key=lambda x: x[1], reverse=False)
        for i in range(min(self.num_of_best_points, len(dist))):
            result.append(dist[i])
        return result
  
    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''
    def printAllPathsUtil(self, u, visited, path, cost):
 
        # Mark the current node as visited and store in path
        visited[u]= True
        path.append(u)
 
        # If current vertex is same as destination, then print
        # current path[]
        if len(path) == len(self.list_dustbin):
            if cost < self.best_distance:
                self.best_distance = cost
                self.best_path = path.copy()
                #self.best_path = path
        else:
            # If current vertex is not destination
            #Recur for all the vertices adjacent to this vertex
            best_points = self.find_best_points(path)
            for point in best_points:
                if visited[point[0]]==False and cost + point[1] < self.best_distance:
                    self.printAllPathsUtil(point[0], visited, path, cost + point[1])
                     
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u]= False
  
  
    # Prints all paths from 's' to 'd'
    def printAllPaths(self):
 
        # Mark all the vertices as not visited
        visited =[False]*len(self.list_dustbin)
 
        # Create an array to store paths
        path = []
 
        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(self.first_point, visited, path, 0)
  
  
#This class represents a directed graph 
# using adjacency list representation
class GraphMultipleRoute:  
    def __init__(self, list_dustbins, num_of_best_points, first_points=None):
        #No. of vertices
        self.list_dustbins = list_dustbins
        self.best_distance = sys.maxsize
        self.best_route = []        
        self.list_dustbin = self.list_dustbins[0]
        self.origin_size = len(self.list_dustbin)
        #add first dustbin of another route to first route to easy merge another route
        for index in range(1, len(list_dustbins)):
            if first_points:
                self.list_dustbin.append(self.list_dustbins[index][first_points[index]])
            else:
                self.list_dustbin.append(self.list_dustbins[index][0])
        # extend route include route 0, first point of another route an another element of there route
        self.extend_route = self.list_dustbin.copy()
        for i in range(1, len(self.list_dustbins)):
            self.extend_route += self.list_dustbins[i][1:]
        self.num_of_best_points = num_of_best_points
        self.first_point = 0
        self.best_path = []

    def get_point_info(self):
        return self.extend_route
        
    def print_best_route(self):
        self.printAllPaths()
        print(self.best_distance)
  #      print("pathsssssssssssssssssss:",self.best_path)
        
    def get_best_route(self):
        self.print_best_route()
        #print("extent route:",self.extend_route)
        #print("best_path:", self.best_path)
        return [self.extend_route[index]for index in self.best_path]

    def find_best_points(self, list_point_had_search):
        """list_point_had_search is a list index of points have searched, return value is a list tupe of (index, and distance)"""
        dist = []
        point = self.extend_route[list_point_had_search[-1]]
        result = []
        for i in range(len(self.extend_route)):
            if i < len(self.list_dustbin):
                if i not in list_point_had_search:
                    dist.append((i, point.distanceHaversineTo(self.extend_route[i])))
            else:
                for j in range(self.origin_size, len(self.list_dustbin)):
                    #index in self.list_dustbins
                    index = j - self.origin_size + 1
                    # start and end index in extend_route
                    start_index = len(self.list_dustbin)
                    end_index = len(self.list_dustbin)
                    
                    for k in range(1, index+1):
                        start_index = end_index
                        end_index = start_index + len(self.list_dustbins[k][1:])
                    if j in list_point_had_search and i >= start_index and i < end_index:
                        if i not in list_point_had_search:
                            dist.append((i, point.distanceHaversineTo(self.extend_route[i])))
        dist.sort(key=lambda x: x[1], reverse=False)
        for i in range(min(self.num_of_best_points, len(dist))):
            result.append(dist[i])
        return result
  
    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''
    def printAllPathsUtil(self, u, visited, path, cost):
 
        # Mark the current node as visited and store in path
        visited[u]= True
        path.append(u)
 
        # If current vertex is same as destination, then print
        # current path[]
        if len(path) == len(self.extend_route):
            if cost < self.best_distance:
                self.best_distance = cost
                self.best_path = path.copy()
        else:
            # If current vertex is not destination
            #Recur for all the vertices adjacent to this vertex
            best_points = self.find_best_points(path)
            for point in best_points:
                if visited[point[0]]==False and cost + point[1] < self.best_distance:
                    self.printAllPathsUtil(point[0], visited, path, cost + point[1])
                     
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u]= False
  
  
    # Prints all paths from 's' to 'd'
    def printAllPaths(self):
 
        # Mark all the vertices as not visited
        visited =[False]*len(self.extend_route)
 
        # Create an array to store paths
        path = []
 
        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(self.first_point, visited, path, 0)
  






# points0 = [(10.775979, 106.647416), (10.778877, 106.645034), (10.778998, 106.646461), (10.778280, 106.647274),
#           (10.778584, 106.649881)]
# points1 = [(10.764792, 106.660616), (10.768143, 106.672997), (10.764433, 106.673684), (10.759311, 106.669414),
#            (10.755664, 106.666732)]
# points2 = [(10.767011, 106.666968), (10.769182, 106.666678), (10.77146, 106.66214), (10.771207, 106.653728)]
# points3 = [(10.754427, 106.646261), (10.75468, 106.656647), (10.757041, 106.652527), (10.751813, 106.653214),
#            (10.751475, 106.641369)]
# list_point = [points0, points1, points2, points3]
# list_first_point = [0, 0, 0, 0]
# list_dustbin = []
# list_dustbins = []
# list_point_had_search = []
# first_point = 0
# num_of_best_points = 1

# for i in range(len(list_point)):
#     #points = list_point[i]
#     list_dustbin = list([])
#     for point in list_point[i]:
#         list_dustbin.append(Dustbin(point[0], point[1]))
#     list_dustbins.append(list(list_dustbin))
    
    
# # Create a graph given in the above diagram
# #for dustbin in list_dustbins[2]:
#     #print(dustbin.getX(), dustbin.getY())
# for dustbin in list_dustbins:
#     print(len(dustbin))
#     u = Graph(dustbin, num_of_best_points, first_point)
#     u.print_best_route()
# #This code is contributed by Neelam Yadav
# g = GraphMultipleRoute(list_dustbins, num_of_best_points, list_first_point)
# g.print_best_route()
