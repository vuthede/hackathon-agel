from src.galogic import *
import src.globals
from pprint import pprint

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
    globals.hash_table_route = {}
    
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
            key = str(s.getLat()) + str(s.getLng()) + str(e.getLat()) + str(e.getLng())
            res = globals.hash_table_route[key]
            sub_routes += route2points(res)
        routes.append(sub_routes)
    
    return routes
            
   
