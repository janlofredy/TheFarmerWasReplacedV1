from helpers import *
import multi_till
droneId = None
def prepare():
    flyTo(0,0)
    if(get_ground_type() != Grounds.Soil):
        multi_till.startTill()
def plantPumpkin():
    plant(Entities.Cactus)

def bubbleSortVertical():
    global droneId
    # Make Sure to start at top
    longFlyTo(droneId, get_world_size()-1)
    for i in range(1, get_world_size() // 2 + 1):
        # Bubble Down
        # sorted = True
        for _ in range(get_world_size() - ((i * 2) -1)):
            if measure() < measure(South):
                swap(South)
                # sorted = False
            else:
                use_item(Items.Water)
                # change_hat(ALL_HATS[droneId % len(ALL_HATS)])
            move(South)
        # if sorted:
        #     break
        move(North)
        # Bubble Up
        for _ in range(get_world_size() - (i * 2)):
            if measure() > measure(North):
                swap(North)
                # sorted = False
            else:
                use_item(Items.Water)
                # change_hat(ALL_HATS[droneId % len(ALL_HATS)])
            move(North)
        # if sorted:
        #     break
        move(South)
    flyTo(droneId, (get_world_size()-1))

def bubbleSortHorizontal():
    global droneId
    # Make Sure to start at Left
    longFlyTo(0, droneId)
    for i in range(1, get_world_size() // 2 + 1):
        # Bubble Right
        sorted = True
        for _ in range(get_world_size() - ((i * 2) -1)):
            if measure() > measure(East):
                swap(East)
                sorted = False
            # else:
            #     change_hat(ALL_HATS[droneId % len(ALL_HATS)])
            move(East)
        if sorted:
            break
        move(West)
        # Bubble Left
        for _ in range(get_world_size() - (i * 2)):
            if measure() < measure(West): 
                swap(West)
                sorted = False
            # else:
            #     change_hat(ALL_HATS[droneId % len(ALL_HATS)])
            move(West)
        if sorted:
            break
        move(East)
    flyTo(0, droneId)

def plantAndHarvest():
    global droneId
    droneId = get_pos_x()
    jobDownwards(plantPumpkin)
    bubbleSortVertical()
    bubbleSortHorizontal()


def collect():
    drones = spawnDronesSimultaneously(plantAndHarvest)
    while num_drones() > 1:
        pass
    harvest()

def mainLoop():
    prepare()
    # while True:
    #     collect()
    collect()

if __name__ == "__main__":
    mainLoop()