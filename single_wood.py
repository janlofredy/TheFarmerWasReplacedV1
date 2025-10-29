from helpers import jobEverywhere
# mode 1
def plantBushOnly():
    plant(Entities.Bush)
    if can_harvest():
        harvest()
# mode 2
def plantBushAndTree():
    x = get_pos_x()
    y = get_pos_y()
    if can_harvest():
        harvest()
    if ( x + y ) % 2 == 0:
        plant(Entities.Tree)
    else:
        plant(Entities.Bush)
# mode 3
def plantHayAndTree():
    x = get_pos_x()
    y = get_pos_y()
    if can_harvest():
        harvest()
    if ( x + y ) % 2 == 0:
        plant(Entities.Tree)
    #    use_item(Items.Fertilizer)
def prepare():
    clear()
def mainLoop():
    clear()
    mode = 2
    # BUSH ONLY MODE
    if mode == 1:
        while True:
            if num_items(Items.Wood) >= 500000000:
                break
            jobEverywhere(plantBushOnly)
    elif mode == 2:
        while True:
            if num_items(Items.Wood) >= 500000000:
                break
            jobEverywhere(plantBushAndTree)
    else:
        # BUSH AND TREE MODE
        while True:
            if num_items(Items.Wood) >= 500000000:
                break
            jobEverywhere(plantHayAndTree)
if __name__ == "__main__":
    mainLoop()