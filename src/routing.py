from random import shuffle
from src.galogic import *
import src.globals
from pprint import pprint
from src.routemanager import RouteManager
from src.helper import route
from src.multiple_helper import GraphMultipleRoute
#hash_table_route = {}


# def real_distance(lon1, lat1, lon2, lat2):
#     key = str(lat1) + str(lon1) + str(lat2) + str(lon2)
#     if key in list(RouteManager.hash_table_route.keys()):
#         return RouteManager.hash_table_route[key]['distance']
    
#     res = route((lat1, lon1), (lat2, lon2))
#     if res != {}:
#         RouteManager.hash_table_route[str(lat1) + str(lon1) + str(lat2) + str(lon2)] = res
#         return res['distance']
    
#     return 0.0


def route2points(route):
    points = []
    path = route['path']
    for segs in path:
        segments = segs['segments']
        for seg in segments:
            middle_point_lat = (seg['lat1'] + seg['lat2']) / 2.0
            middle_point_lng = (seg['lng1'] + seg['lng2']) / 2.0
            points.append((middle_point_lat, middle_point_lng, False))

    points[0] = (points[0][0], points[0][1], True) 
    points[-1] = (points[-1][0], points[-1][1], True)
    
    return points



def group_by_source(list_dustbins):
   # print("list dustbin:...................", list_dustbins)
    def distance(dustbins):
        sum = 0
        for i in range(1, len(dustbins)):
            sum += dustbins[i-1].distanceTo(dustbins[i])
        return sum
    
    result = []
    
    p = list_dustbins.pop()
    if not list_dustbins:
        result.append(p)
        
    while(list_dustbins):
        first = list_dustbins[-1]
        graph = GraphMultipleRoute([p, first], 1)
        combine_route = graph.get_best_route()
       #print("combine: ", combine_route)
        
        if(distance(combine_route) < distance(p) + distance(first) and len(combine_route) < 5):
            p = combine_route
            list_dustbins.pop()
            continue
        else:
        #    print("hereeeeeeeeeeeeeeee")
            result.append(p)
            
        if len(list_dustbins) == 0:
            break
        if len(list_dustbins) == 1:
            result.append(list_dustbins.pop())
            break
        
        p =  list_dustbins.pop()
    if (len(result) == 0):
        result.append(p)
    return result
       
        
        
            
   
def multiple_source_routing(list_points, max_num_trucks=3):
    def distance(list_dustbins):
        total = 0
        for dustbins in list_dustbins:
            sum = 0
            for i in range(1, len(dustbins)):
                sum += dustbins[i-1].distanceTo(dustbins[i])
            total += sum
            
        return total
    
    # Find best routes for each source                   
    best_route_from_sources = []
  #  print("Before merge...........................")
#     print("this is list points:", list_points[0])
    for points in list_points:
#         print("this is points:", points)
        globalRoute = find_best_route_for_single_source(points, numTrucks=1)
        best_route_from_sources.append(globalRoute.route)
    
   # print("After merge...........................")
    # Merge routes from different sources
    flatten_routes = []
    #print("best_routesss:", best_route_from_sources)
    for r in best_route_from_sources:
        flatten_routes += r
    
    optimal = []
    optimal_distance = 1000
    for i in range(1, 10):
        shuffle(flatten_routes)
       #print("flatten:" ,flatten_routes)
        group = group_by_source(flatten_routes.copy())
    #    print("group:", group)
        if (distance(group) < optimal_distance):
            optimal_distance = distance(group)
            optimal = group
    
  #  print("Caculating practice  distance.................")
      
     # Create route for each shipper.
 #   print("optimal:", optimal)
    routes = []
    for i in range(len(optimal)):
        sub_routes = []
        for j in range(len(optimal[i]) -1):  # route length have to be greater than 2.
            s = optimal[i][j]
            e = optimal[i][j+1]
            #key = str(s.getLat()) + str(s.getLng()) + str(e.getLat()) + str(e.getLng())
            #res = RouteManager.hash_table_route[key]
            #print("find routesssss...")
            res = route((s.getLat(), s.getLng()), (e.getLat(), e.getLng()))
            sub_routes += route2points(res)
        routes.append(sub_routes)
    print(routes)
    
    return routes

    
def find_best_route_for_single_source(points, numTrucks):
    RouteManager.resetDustbins()
   # print("leng init dusbin:", RouteManager.numberOfDustbins())
    for p in points:
        RouteManager.addDustbin(Dustbin(p[0], p[1])) # p[0]: lat, p[1]: lng
        RouteManager.initNumTrucks(numTrucks)
    Population.routes = []   
    pop = Population(populationSize, True)
    
    #print("route lengh:", len(pop.routes))
    globalRoute = pop.getFittest()
   # print ('Initial minimum distance: ' + str(globalRoute.getDistance()))
    
    # Start evolving
    for i in range(0, numGenerations):
        pop = GA.evolvePopulation(pop)
        localRoute = pop.getFittest()
        if globalRoute.getDistance() > localRoute.getDistance():
            globalRoute = localRoute
            
    return globalRoute
    

def single_source_routing(points, numTrucks):
    """Return best routes for each shipper from single source
    
        @params:
            + points: group of point (lat, lng).
            + numTrucks: number of shippers
        
        @return:
            An 2-D arrays represent for best route of each shipper. 
            The route of each shipper has form like this [(lat1, lng1, "boolean"), ......, (latn, lngn, "boolean")]
            "Boolean = True" means destination. "Boolean = False" means non-destination.
            
    """
    
    # Reset hash_table
    #init_hash_table()
    
    for p in points:
        RouteManager.addDustbin(Dustbin(p[0], p[1])) # p[0]: lat, p[1]: lng
        RouteManager.initNumTrucks(numTrucks)
        
    pop = Population(populationSize, True)
    globalRoute = pop.getFittest()
    print ('Initial minimum distance: ' + str(globalRoute.getDistance()))
    
    # Start evolving
    for i in range(0, numGenerations):
        pop = GA.evolvePopulation(pop)
        localRoute = pop.getFittest()
        if globalRoute.getDistance() > localRoute.getDistance():
            globalRoute = localRoute
       
    
    # Create route for each shipper.
    routes = []
    for i in range(RouteManager.getNumTrucks()):
        sub_routes = []
        for j in range(globalRoute.routeLengths[i] -1):  # route length have to be greater than 2.
            s = globalRoute.getDustbin(i,j)
            e = globalRoute.getDustbin(i,j+1)
            #key = str(s.getLat()) + str(s.getLng()) + str(e.getLat()) + str(e.getLng())
            #res = RouteManager.hash_table_route[key]
            res = route((s.getLat(), s.getLng()), (e.getLat(), e.getLng()))
            sub_routes += route2points(res)
        routes.append(sub_routes)
    
    return routes
            
   
