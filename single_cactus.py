from helpers import *
from single_till import startTill

def plantCactus():
    plant(Entities.Cactus)

def prepare():
    set_world_size(8)
    flyTo(0,7)
    if(get_ground_type() != Grounds.Soil):
        startTill()

def sortPlantedCactus():
    # TODO FIX
    # HORIZONTAL SORTING
    for row in range(get_world_size()):
        swapped = False
        for x in range(get_world_size()-2):
            for y in range(get_world_size() - x):
                if measure() > measure(East):
                    swap(East)
                    swapped = True
                move(East)
            move(West)
            if not swapped:
                break
            swapped = False
            flyTo(0, get_world_size()-row-1)
        flyTo(0, get_world_size()-row-1)
    # VERTICAL SORTING
    for col in range(get_world_size()):
        swapped = False
        for y in range(get_world_size()-2):
            for x in range(get_world_size() - y):
                if measure() < measure(South):
                    swap(South)
                    swapped = True
                move(South)
            move(North)
            if not swapped:
                break
            swapped = False
            flyTo(get_world_size()-col-1, 0)
        flyTo(get_world_size()-col-1, 0)


def collectCactus():
    jobEverywhere(plantCactus)
    sortPlantedCactus()
    harvest()

def mainLoop():
    prepare()
    while True:
        collectCactus()

if __name__ == "__main__":
    mainLoop()