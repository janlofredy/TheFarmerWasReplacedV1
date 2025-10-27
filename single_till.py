from helpers import *
def harvestIfPossibleThenTill():
    if can_harvest():
        harvest()
    if get_ground_type() != Grounds.Soil:
        till()
def startTill(): 
    jobEverywhere(harvestIfPossibleThenTill)

if __name__ == "__main__":
    startTill()