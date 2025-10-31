from helpers import *
import multi_till

def prepare():
    flyTo(0,0)
    if(get_ground_type() != Grounds.Soil):
        multi_till.startTill()
        
def plantHarvestCarrot():
    if can_harvest():
        harvest()
    # else:
    #     change_hat(Hats.Straw_Hat)
    plant(Entities.Carrot)
    if get_water() <= .75:
        use_item(Items.Water)
    # else:
    #     change_hat(Hats.Straw_Hat)
def job():
    if __name__ == "__main__":
        while True:
            if num_items(Items.Carrot) >= 2000000000:
                break
            jobDownwards(plantHarvestCarrot)
            # change_hat(Hats.Straw_Hat)
    else:
        jobDownwards(plantHarvestCarrot)
def collectHay():
    spawnDronesSimultaneously(job)

def mainLoop():
    prepare()
    collectHay()

if __name__ == "__main__":
    mainLoop()