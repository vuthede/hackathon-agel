'''
Represents nodes in the problem graph or network.
Locatin coordinates can be passed while creating the object or they
will be assigned random values.
'''
from globals import *
from helper import haversine, real_distance

class Dustbin:
    
    def __init__(self, lat=None, lng=None):
        if lat==None or lng==None:
            raise("Lat or Lng is null!!!")
        self.__lat = lat
        self.__lng = lng
    
    def getLat(self):
        return self.__lat
    
    def getLng(self):
        return self.__lng
    
    def distanceTo (self, db):
        #return haversine(self.getLng(), self.getLat(), db.getLng(), db.getLat())
        return real_distance(self.getLng(), self.getLat(), db.getLng(), db.getLat())

    
    def toString (self):
        s =  '(' + str(self.getLat()) + ',' + str(self.getLng()) + ')'
        return s
    def checkNull(self):
        if self.__lat == -1:
            return True
        else:
            return False


# class Dustbin:
# 	# Good old constructor
# 	def __init__ (self, x = None, y = None):
# 		if x == None and y == None:
# 			self.x = random.randint(0, xMax)
# 			self.y = random.randint(0, yMax)
# 		else:
# 			self.x = x
# 			self.y = y

# 	def getX (self):
# 		return self.x

# 	def getY (self):
# 		return self.y

# 	# Returns distance to the dustbin passed as argument
# 	def distanceTo (self, db):
# 		xDis = abs(self.getX() - db.getX())
# 		yDis = abs(self.getY() - db.getY())
# 		dis = math.sqrt((xDis*xDis) + (yDis*yDis))
# 		return dis

# 	# Gives string representation of the Object with coordinates
# 	def toString (self):
# 		s =  '(' + str(self.getX()) + ',' + str(self.getY()) + ')'
# 		return s

# 	# Check if cordinates have been assigned or not
# 	# Dusbins with (-1, -1) as coordinates are created during creation on chromosome objects
# 	def checkNull(self):
# 		if self.x == -1:
# 			return True
# 		else:
# 			return False
