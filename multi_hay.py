from helpers import *

def prepare():
    flyTo(0,0)
    clear()
def harvestIfPossible():
    if can_harvest():
        harvest()
def job():
    if __name__ == "__main__":
        while True:
            if num_items(Items.Carrot) >= 2000000000:
                break
            jobDownwards(harvestIfPossible)
    else:
        jobDownwards(harvestIfPossible)
def collectHay():
    spawnDronesSimultaneously(job)

def mainLoop():
    prepare()
    collectHay()

if __name__ == "__main__":
    mainLoop()