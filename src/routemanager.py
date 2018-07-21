'''
Holds all the dustbin objects and is used for
creation of chromosomes by jumbling their sequence
'''
from src.dustbin import *

class RouteManager:
    hash_table_route = {}
    destinationDustbins = []
    numTrucks = None
    
    @classmethod
    def initNumTrucks (cls, numTrucks):
        cls.numTrucks = numTrucks
        
    @classmethod
    def getNumTrucks (cls):
        return cls.numTrucks 
    
    
    @classmethod
    def addDustbin (cls, db):
        cls.destinationDustbins.append(db)

    @classmethod
    def getDustbin (cls, index):
        return cls.destinationDustbins[index]

    @classmethod
    def numberOfDustbins(cls):
        return len(cls.destinationDustbins)
