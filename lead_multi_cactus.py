from helpers import *
# droneId = None
worldSize =  get_world_size()
maxWorldIndex = worldSize-1
def plantAndSortHorizontalDrones():
    # global droneId
    # droneId = get_pos_x()
    for i in range(worldSize):
        if get_ground_type() != Grounds.Soil:
            till()
        plant(Entities.Cactus)
        if i > 0:
            if measure(South) and measure() < measure(South):
                swap(South)
        move(North)
    # bubbleUpandDown
    droneY = 0
    top = maxWorldIndex-1
    bottom = 0
    lastTopSorted = bottom
    lastBottomSorted = top
    while True:
        sorted = True
        # Bubble Up
        while droneY < top:
            if measure() > measure(North):
                swap(North)
                sorted = False
                lastTopSorted = top
            move(North)
            droneY += 1
        top = lastTopSorted - 1
        if sorted:
            break
        while droneY > bottom:
            if measure() < measure(South):
                swap(South)
                sorted = False
                lastBottomSorted = bottom
            move(South)
            droneY -= 1
        bottom = lastBottomSorted + 1
        if sorted:
            break


def sortVerticalDrones():
    droneX = 0
    right = maxWorldIndex
    left = 0
    lastRightSorted = left
    lastLeftSorted = right
    while True:
        sorted = True
        # Bubble Up
        while droneX < right:
            if measure() > measure(East):
                swap(East)
                sorted = False
                lastRightSorted = right
            move(East)
            droneX += 1
        right = lastRightSorted - 1 
        if sorted:
            break
        while droneX > left:
            if measure() < measure(West):
                swap(West)
                sorted = False
                lastLeftSorted = left
            move(West)
            droneX -= 1
        left = lastLeftSorted + 1
        if sorted:
            break
gridMap = [
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4], 
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5], 
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5], 
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5], 
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5], 
    [0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5], 
    [0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5], 
    [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6], 
    [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6], 
    [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6], 
    [1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6], 
    [1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6], 
    [1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6], 
    [2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6], 
    [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7], 
    [2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7], 
    [2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7], 
    [2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7], 
    [2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7], 
    [3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7], 
    [3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8], 
    [3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8], 
    [3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8], 
    [3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8], 
    [3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8], 
    [3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8], 
    [4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9], 
    [4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9], 
    [4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9], 
    [4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9], 
    [4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9], 
    [4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9]]
def cactusRepottingDroneJob():
    droneX = get_pos_x()
    for droneY in range(worldSize):
        if get_ground_type() != Grounds.Soil:
            till()
        # plant(Entities.Cactus)
        move(North)
    for droneY in range(worldSize):
        while True:
            plant(Entities.Cactus)
            heuristicSize = gridMap[droneX][droneY]
            leftHeuristicSize = None
            # ALREADY PLANTED MEASURES
            cactiSize = measure()
            left = measure(West)
            right = measure(East)
            up = measure(North) # can be none if not planted yet
            down = measure(South) 
            if cactiSize == heuristicSize:
                break
            if droneX > 0:
                leftHeuristicSize = gridMap[droneX-1][droneY]
                if left != leftHeuristicSize and cactiSize == leftHeuristicSize: 
                    swap(West)
            if droneX < maxWorldIndex:
                rightHeuristicSize = gridMap[droneX+1][droneY]
                if right != rightHeuristicSize and cactiSize == rightHeuristicSize: 
                    swap(East)
            if droneY < maxWorldIndex:
                upHeuristicSize = gridMap[droneX][droneY+1]
                if up != upHeuristicSize and cactiSize == upHeuristicSize:
                    swap(North)
            till() # to grassland
            till() # to soil
        move(North)
    if measure(West) == None:
        move(West)
        droneX = get_pos_x()
        for droneY in range(droneY, -1, -1):
            move(South)
            while True:
                plant(Entities.Cactus)
                heuristicSize = gridMap[droneX][droneY]
                leftHeuristicSize = None
                # ALREADY PLANTED MEASURES
                cactiSize = measure()
                left = measure(West)
                right = measure(East)
                up = measure(North) # can be none if not planted yet
                down = measure(South) 
                if cactiSize == heuristicSize:
                    break
                if droneX > 0:
                    leftHeuristicSize = gridMap[droneX-1][droneY]
                    if left != leftHeuristicSize and cactiSize == leftHeuristicSize: 
                        swap(West)
                if droneX < maxWorldIndex:
                    rightHeuristicSize = gridMap[droneX+1][droneY]
                    if right != rightHeuristicSize and cactiSize == rightHeuristicSize: 
                        swap(East)
                if droneY < maxWorldIndex:
                    upHeuristicSize = gridMap[droneX][droneY+1]
                    if up != upHeuristicSize and cactiSize == upHeuristicSize:
                        swap(North)
                till() # to grassland
                till() # to soil

# harvest()
# clear()
# flyTo(30, 5)
# print(measure(), gridMap[get_pos_x()][get_pos_y()], measure(West), measure(South), measure(East))
# flyTo(0, 0)
# drones = spawnDronesLine(cactusRepottingDroneJob)
# for drone in drones:
#     wait_for(drone)
# harvest()


def justPlant():
    for droneY in range(worldSize):
        if get_ground_type() != Grounds.Soil:
            till()
        # plant(Entities.Cactus)
        if droneY < worldSize - 1:
            move(North)
# drones = spawnDronesLine(justPlant)
# drones = spawnDronesSimultaneously(justPlant)
drones = spawnDronesSimultaneouslyFun(cactusRepottingDroneJob)
for drone in drones:
    wait_for(drone)
do_a_flip()
harvest()