from helpers import *

def harvestIfPossibleThenTill():
    if can_harvest():
        harvest()
    if get_ground_type() != Grounds.Soil:
        till()
def job():
    jobDownwards(harvestIfPossibleThenTill)

def startTill():
    spawnDronesSimultaneously(job)

if __name__ == "__main__":
    startTill()