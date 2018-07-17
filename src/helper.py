from math import radians, cos, sin, asin, sqrt
import urllib.request
import json
import numpy as np
import globals


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km


def route(start, end):
    if start == (-1, -1) or end == (-1, -1):
        return {}

    seg = "https://traffic.hcmut.edu.vn/ITS/rest/segment_id/"
    direct = "https://traffic.hcmut.edu.vn/ITS/rest/motor/distance_dijkstra1/"
  
    #print("start: {}, end: {}".format(start, end))
    #try: 
    src = urllib.request.urlopen(seg+ str(start[0])+'/' + str(start[1])).read()
    src_id = json.loads(src.decode("utf-8"))['segment_id']
    #except:
     #   print("Failed in point: {}".format((start[0], start[1])))
        
    #try:
    dest = urllib.request.urlopen(seg+ str(end[0])+'/' + str(end[1])).read()
    dest_id = json.loads(dest.decode("utf-8"))['segment_id']
    #except:
     #   print("Failed in point: {}".format((dest[0], dest[1])))
        
    route = urllib.request.urlopen(direct+ str(start[0])+'/' + str(start[1]) 
                                   + '/'+str(src_id)+'/' + str(end[0])+'/' + str(end[1]) 
                                   + '/'+str(dest_id)).read()
    
    data_route = json.loads(route.decode("utf-8"))
    
    return data_route
    



def real_distance(lon1, lat1, lon2, lat2):
    key = str(lat1) + str(lon1) + str(lat2) + str(lon2)
    if key in list(globals.hash_table_route.keys()):
        return globals.hash_table_route[key]['distance']
    
    res = route((lat1, lon1), (lat2, lon2))
    if res != {}:
        globals.hash_table_route[str(lat1) + str(lon1) + str(lat2) + str(lon2)] = res
        return res['distance']
    
    return 0.0
    
    



