import sys
sys.path.insert(0, '../src')
import time
from routing import single_source_routing
from pprint import pprint



if __name__ == "__main__":
    start_time = time.time()
    
    points = [(10.775979, 106.647416), (10.778877, 106.645034), (10.778998, 106.646461), (10.778280, 106.647274),
          (10.778584, 106.649881), (10.779987, 106.650601), (10.779507, 106.649450), (10.779073, 106.650368)]
    numTrucks = 3
    routes = single_source_routing(points = points, numTrucks = numTrucks)
    print("This is best routes:\n")
    pprint(routes)
    
    print("--- %s seconds ---" % (time.time() - start_time))