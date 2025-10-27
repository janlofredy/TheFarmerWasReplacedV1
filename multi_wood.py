from helpers import *

def prepare():
    flyTo(0,0)
    # clear()
        
def plantHayAndTree():
    x = get_pos_x()
    y = get_pos_y()
    if can_harvest():
        harvest()
    else:
        change_hat(Hats.Straw_Hat)
    if get_ground_type() != Grounds.Soil:
        till()
    # else:
    #     change_hat(Hats.Straw_Hat)
    if ( x + y ) % 2 == 0:
        if get_water() <= .75:
            use_item(Items.Water)
        else:
            change_hat(Hats.Straw_Hat)
        plant(Entities.Tree)
        # use_item(Items.Fertilizer)
    else:
        plant(Entities.Bush)
        # if get_ground_type() == Grounds.Soil:
        #     till()
        # else:
        #     change_hat(Hats.Straw_Hat)
def job():
    if __name__ == "__main__":
        # while True:
        while True:
            if num_items(Items.Wood) >= 10000000000:
                break
            jobDownwards(plantHayAndTree)
            change_hat(Hats.Straw_Hat)
    else:
        jobDownwards(plantHayAndTree)
def collectHay():
    spawnDronesSimultaneously(job)

def mainLoop():
    # prepare()
    collectHay()

if __name__ == "__main__":
    mainLoop()