from helpers import *
# droneId = None
worldSize =  get_world_size()
maxWorldIndex = worldSize-1
def plantAndSortHorizontalDrones():
    # global droneId
    # droneId = get_pos_x()
    # for i in range(worldSize):
    #     if get_ground_type() != Grounds.Soil:
    #         till()
    #     plant(Entities.Cactus)
    #     if i > 0:
    #         if measure(South) and measure() < measure(South):
    #             swap(South)
    #         else:
    #             change_hat(Hats.Straw_Hat)
    #     move(North)
    # bubbleUpandDown
    droneY = 0
    top = maxWorldIndex
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
    move(North)


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
                    continue
            if droneX < maxWorldIndex:
                rightHeuristicSize = gridMap[droneX+1][droneY]
                if right != rightHeuristicSize and cactiSize == rightHeuristicSize: 
                    swap(East)
                    continue
            if droneY < maxWorldIndex:
                upHeuristicSize = gridMap[droneX][droneY+1]
                if up != upHeuristicSize and cactiSize == upHeuristicSize:
                    swap(North)
                    continue
            if cactiSize <= heuristicSize+1 and cactiSize >= heuristicSize-1:
                break
            till() # to grassland
            till() # to soil
        move(North)
def cactusRepottingV2DroneJob():
    size = 32 * 2
    tolerance = 1.5
    num_values = 10
    droneX = get_pos_x()
    for droneY in range(worldSize):
        if get_ground_type() != Grounds.Soil:
            till()
        plant(Entities.Cactus)
        move(North)
    for droneY in range(worldSize):
        while True:
            cactiSize = measure()
            segment_size = size / num_values
            base_min = cactiSize * segment_size
            base_max = (cactiSize + 1) * segment_size

            tol = segment_size * tolerance
            min_allowed = max(0, base_min - tol)
            max_allowed = min(size, base_max + tol)

            if min_allowed <= (droneX+droneY) <= max_allowed:
                break
            till() # to grassland
            till() # to soil
            plant(Entities.Cactus)
        move(North)

# harvest()
# clear()
# flyTo(30, 5)
# print(measure(), gridMap[get_pos_x()][get_pos_y()], measure(West), measure(South), measure(East))
# flyTo(0, 0)
# drones = spawnDronesLine(cactusRepottingDroneJob)
# for drone in drones:
#     wait_for(drone)
# harvest()
def find_median(vs):
    # Simple selection sort for 5 values
    for i in range(4):
        for j in range(i+1, 5):
            if vs[j] < vs[i]:
                vs[i], vs[j] = vs[j], vs[i]
    return vs[2]  # middle value

def sort_plus_shape():
    # Step 1: Measure all values
    center = measure()
    north = measure(North)
    south = measure(South)
    east = measure(East)
    west = measure(West)
    values = [center, north, south, east, west]
    # Step 2: Find median manually
    median = find_median(values[:])  # use copy to avoid mutating original
    # Step 3: Move median to center
    if center != median:
        if north == median:
            swap(North)
            center = median
            north = measure(North)
        elif south == median:
            swap(South)
            center = median
            south = measure(South)
        elif east == median:
            swap(East)
            center = median
            east = measure(East)
        elif west == median:
            swap(West)
            center = median
            west = measure(West)
    # Step 4: Identify highs and lows
    highs = []
    lows = []
    for v in [north, south, east, west]:
        if v > center:
            highs.append(v)
        elif v < center:
            lows.append(v)
    # Step 5: Place highs in North and East
    for direction in [North, East]:
        val = measure(direction)
        if val <= center:
            for alt in [South, West]:
                alt_val = measure(alt)
                if alt_val > center:
                    swap(alt)
                    swap(direction)
                    break
    # Step 6: Place lows in South and West
    for direction in [South, West]:
        val = measure(direction)
        if val >= center:
            for alt in [North, East]:
                alt_val = measure(alt)
                if alt_val < center:
                    swap(alt)
                    swap(direction)
                    break




def spawnBubbleSort():
    move(West)
    while get_pos_x() < maxWorldIndex:
        if measure() > measure(East):
            swap(East)
        move(East)
        spawn_drone(spawnBubbleSort)
    move(North)

def lineSpamSort():
    # global droneId
    # droneId = get_pos_x()
    # for i in range(worldSize):
    #     if get_ground_type() != Grounds.Soil:
    #         till()

    #     plant(Entities.Cactus)
    #     # if i > 0:
    #     #     if measure(South) and measure() < measure(South):
    #     #         swap(South)
    #     #     else:
    #     #         change_hat(Hats.Straw_Hat)
    #     move(North)
    while get_pos_y() < maxWorldIndex:
        for i in range(maxWorldIndex//2):
            if get_pos_x() < maxWorldIndex:
                if measure(East) != None and measure() > measure(East):
                    swap(East)
                else:
                    change_hat(Hats.Straw_Hat)
                # sort_plus_shape()
            else:
                # if measure(West) and measure() < measure(West):
                #     swap(West)
                # else:
                #     change_hat(Hats.Straw_Hat)
                change_hat(Hats.Straw_Hat)
        move(North)
    for i in range(maxWorldIndex//2):
        if get_pos_x() < maxWorldIndex:
            if measure(East) != None and measure() > measure(East):
                swap(East)
            else:
                change_hat(Hats.Straw_Hat)
            # sort_plus_shape()
        else:
            # if measure(West) and measure() < measure(West):
            #     swap(West)
            # else:
            #     change_hat(Hats.Straw_Hat)
            change_hat(Hats.Straw_Hat)
    move(North)


def justPlant():
    for droneY in range(worldSize):
        if get_ground_type() != Grounds.Soil:
            till()
        plant(Entities.Cactus)
        # if droneY < worldSize - 1:
        #     move(North)
        move(North)
def justMoveUp():
    for _ in range(worldSize):
        move(North)
        change_hat(Hats.Straw_Hat)
        change_hat(Hats.Straw_Hat)
        change_hat(Hats.Straw_Hat)
        change_hat(Hats.Straw_Hat)
def sortJob():
    lineSpamSort()
    plantAndSortHorizontalDrones()

# drones = spawnDronesFastest(justPlant)
# while num_drones() > 1:
#     pass
# drones = spawnDronesFastest(lineSpamSort)
# while num_drones() > 1:
#     pass
while num_items(Items.Cactus) < 33554432:
    drones = spawnDronesFastest(cactusRepottingV2DroneJob)
    while num_drones() > 1:
        pass
    drones = spawnDronesFastest(sortJob)
    while num_drones() > 1:
        pass
    # drones = spawnDronesFastest(justMoveUp)
    # while num_drones() > 1:
    #     pass
    harvest()
