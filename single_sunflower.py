import single_till
from helpers import *
sunflowersPetals = [[],[],[],[],[],[],[],[],[]]
def plantSunflowerAndMap():
    global sunflowersPetals
    plant(Entities.Sunflower)
    while get_water() <= .75:
        use_item(Items.Water)
    sunflowersPetals[15-measure()].append( (get_pos_x(), get_pos_y()) ) 
def prepare():
    flyTo(0,0)
    if(get_ground_type() != Grounds.Soil):
        single_till.startTill()
def collectSunflowers():
    global sunflowersPetals
    # RESET MAP
    sunflowersPetals = [[],[],[],[],[],[],[],[],[]]
    jobEverywhere(plantSunflowerAndMap)
    while True:
        if len(sunflowersPetals) == 0:
            break
        currentPetals = sunflowersPetals.pop(0)
        while True:
            if len(currentPetals) == 0:
                break
            curSunflower = currentPetals.pop(0)
            flyTo(curSunflower[0], curSunflower[1])
            if can_harvest():
                harvest()
            else:
                currentPetals.append(curSunflower)
def mainLoop():
    prepare()
    while True:
        if num_items(Items.Power) >= 10000:
            break
        collectSunflowers()
    
if __name__ == "__main__":
    mainLoop()
