from helpers import *
# you think they could be synced? or sync most likely not required?

worldSize =  get_world_size()
maxWorldIndex = worldSize-1
def cactusRepottingSameRatioDroneJob():
    size = 32
    tolerance = 2
    num_values = 10
    droneX = get_pos_x()
    limitCounts01 = 4
    limitCountsOther = 3
    counts = [0,0,0,0,0,0,0,0,0,0]
    planted = 0
    maxSize = 3
    for droneY in range(worldSize):
        if get_ground_type() != Grounds.Soil:
            till()
        while True:
            plant(Entities.Cactus)
            cactiSize = measure()
            if cactiSize <= maxSize:
                if cactiSize < 2:
                    if counts[cactiSize] < limitCounts01:
                        counts[cactiSize] += 1
                        planted = (planted + 1) % 4
                        if planted == 3:
                            maxSize += 1
                        break
                else:
                    if counts[cactiSize] < limitCountsOther:
                        counts[cactiSize] += 1
                        planted = (planted + 1) % 4
                        if planted == 3:
                            maxSize += 1
                        break
            till()
            till()
        move(North)
    #shaker sort
    top = maxWorldIndex
    bottom = 0
    swapped = True
    yLoc = 0
    while swapped:
        swapped = False
        lastTopSorted = top
        while yLoc < top:
            if measure() > measure(North):
                swap(North)
                swapped = True
                lastTopSorted = yLoc
            yLoc += 1
            move(North)
        if not swapped:
            break
        top = lastTopSorted
        lastBottomSorted = bottom
        while yLoc > bottom:
            if measure() < measure(South):
                swap(South)
                swapped = True
                lastBottomSorted = yLoc
            yLoc -= 1
            move(South)
        bottom = lastBottomSorted


spawnDronesFastest(cactusRepottingSameRatioDroneJob)
while num_drones() > 1:
    pass
harvest()
