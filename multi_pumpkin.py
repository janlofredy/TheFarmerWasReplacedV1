from helpers import *
import multi_till
unharvestablePumpkins = []
def plantPumpkin():
    if(get_ground_type() != Grounds.Soil):
        till()
    plant(Entities.pumpkin)
    # if get_water() <= .50 and num_items(Items.Water) > 0:
    #     use_item(Items.Water)
    # else:
    #     change_hat(Hats.Straw_Hat)
def mapUnharvestablePumpkin():
    global unharvestablePumpkins
    # pos = (get_pos_x(), get_pos_y())
    if not can_harvest():
        plant(Entities.Pumpkin)
        if get_water() <= .75 and num_items(Items.Water) > 0:
            use_item(Items.Water)
        # if len(unharvestablePumpkins) == 1 and num_items(Items.Fertilizer) > 0:
        #     use_item(Items.Fertilizer)
        # unharvestablePumpkins.append(pos)
        unharvestablePumpkins.append(get_pos_y())
def prepare():
    # flyTo(0,0)
    if(get_ground_type() != Grounds.Soil):
        multi_till.startTill()
def plantAndHarvest():
    global unharvestablePumpkins
    jobDownwards(plantPumpkin)
    jobDownwards(mapUnharvestablePumpkin)
    while True:
        if len(unharvestablePumpkins) == 0:
            break
        toCheck = unharvestablePumpkins.pop(0)
        while get_pos_y() > toCheck:
            move(South)
        while get_pos_y() < toCheck:
            move(North)
        if not can_harvest():
            # unharvestablePumpkins.append((get_pos_x(), get_pos_y()))
            unharvestablePumpkins.append(get_pos_y())
            plant(Entities.Pumpkin)

def collect():
    drones = spawnDronesSimultaneously(plantAndHarvest)
    for drone in drones:
        wait_for(drone)
    harvest()

def mainLoop():
    prepare()
    while True: 
        if num_items(Items.Pumpkin) >= 200000000:
            break
        collect()
    # while True:
    #     collect()

if __name__ == "__main__":
    mainLoop()