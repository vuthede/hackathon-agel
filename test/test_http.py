import urllib.request
import json

seg = "https://traffic.hcmut.edu.vn/ITS/rest/segment_id/"
direct = "https://traffic.hcmut.edu.vn/ITS/rest/motor/distance_dijkstra1/"
def route(start, end):
    src = urllib.request.urlopen(seg+ str(start[0])+'/' + str(start[1])).read()
    src_id = json.loads(src.decode("utf-8"))['segment_id']
    
    dest = urllib.request.urlopen(seg+ str(end[0])+'/' + str(end[1])).read()
    dest_id = json.loads(dest.decode("utf-8"))['segment_id']


    route = urllib.request.urlopen(direct+ str(start[0])+'/' + str(start[1]) + '/'+str(src_id)+'/' + str(end[0])+'/' + str(end[1]) + '/'+str(dest_id)).read()
    data_route = json.loads(route.decode("utf-8"))
    print(src_id)
    print(dest_id)
    print(data_route)
    

