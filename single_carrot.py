import single_till
from helpers import *
def harvestThenPlantCarrot():
    if can_harvest():
        harvest()
    plant(Entities.Carrot)
    while get_water() <= .75:
        use_item(Items.Water)
def prepare():
    flyTo(0,0)
    if(get_ground_type() != Grounds.Soil):
        single_till.startTill()
def collectCarrots():
    jobEverywhere(harvestThenPlantCarrot)
def loop():
    while True:
        if num_items(Items.Carrot) >= 100000000:
            break
        collectCarrots()
if __name__ == "__main__":
    prepare()
    loop()