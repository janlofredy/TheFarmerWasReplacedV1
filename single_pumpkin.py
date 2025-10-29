from helpers import *
from single_till import startTill
# ASSUMED WHOLE GRID IS TILLED
# ASSUMED WHOLE GRID IS EMPTY
unharvestablePumpkins = []
def plantPumpkins():
    plant(Entities.Pumpkin)
    while get_water() <= .75:
        use_item(Items.Water)
def mapUnharvestablePumpkins():
    global unharvestablePumpkins
    pos = (get_pos_x(), get_pos_y())
    if not can_harvest():
        plant(Entities.Pumpkin)
        while get_water() <= .75:
            use_item(Items.Water)
        unharvestablePumpkins.append(pos)
def prepare():
    flyTo(0,0)
    if(get_ground_type() != Grounds.Soil):
        startTill()
def collectPumpkins():
    global unharvestablePumpkins
    flyTo(0,0)
    # Plant on whole grid
    jobEverywhere(plantPumpkins)
    unharvestablePumpkins = []
    # MOVE THROUGH WHOLE GRID AND CHECK IF HARVESTABLE
    jobEverywhere(mapUnharvestablePumpkins)
    # LOOP THROUGH UNHARVESTABLE POSITIONS UNTIL ALL HARVESTED
    while True:
        if len(unharvestablePumpkins) == 0:
            break
        toCheck = unharvestablePumpkins.pop(0)
        flyTo(toCheck[0], toCheck[1])
        if not can_harvest():
            unharvestablePumpkins.append((get_pos_x(), get_pos_y()))
            plant(Entities.Pumpkin)
    harvest()
def mainLoop():
    prepare()
    while True:
        if num_items(Items.Pumpkin) >= 10000000:
            break
        collectPumpkins()
if __name__ == "__main__":
    mainLoop()