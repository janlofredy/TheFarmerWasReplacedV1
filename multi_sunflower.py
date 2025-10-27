from helpers import *
import multi_till
petals = 15
def plantSunflowerAndMap():
    plant(Entities.Sunflower)
    if get_water() <= .75:
        use_item(Items.Water)
    else:
        change_hat(Hats.Straw_Hat)
def prepare():
    flyTo(0,0)
    if(get_ground_type() != Grounds.Soil):
        multi_till.startTill()
def harvestByPetals():
    global petals
    if measure() == petals:
        harvest()
    else:
        change_hat(Hats.Straw_Hat)
def plantAndHarvest():
    global petals
    jobDownwards(plantSunflowerAndMap)
    do_a_flip()
    for curPetals in range(15, 6, -1):
        petals = curPetals
        jobDownwards(harvestByPetals)
def job():
    if __name__ == "__main__":
        while True:
            if num_items(Items.Power) >= 100000:
                break
            plantAndHarvest()
    else:
        plantAndHarvest()
def collectHay():
    spawnDronesSimultaneously(job)

def mainLoop():
    prepare()
    collectHay()

if __name__ == "__main__":
    mainLoop()