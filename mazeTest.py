from helpers import *
# set_world_size(5)
flood = None
mazeWalls = []
toUpdateFlood = []
goal = None

def getMinNeighbor(neighbors):
    minNeighbor = []
    minVal = None
    for neighbor in neighbors:
        if minVal == None or neighbor['value'] < minVal:
            minNeighbor = [neighbor]
        if minVal == neighbor['value']:
            minNeighbor.append(neighbor)
    return minNeighbor

def getSortedFloodNeighbors():
    global mazeWalls
    global flood
    currentX = get_pos_x()
    currentY = get_pos_y()
    curVal = flood[currentX][currentY]
    currentCell = (str(currentX)+","+str(currentY))
    if currentX > 0 and flood[currentX - 1][currentY] != None and flood[currentX - 1][currentY] == curVal-1 and West not in mazeWalls[currentCell]:
        return West
    if currentX < maxWorld and flood[currentX + 1][currentY] != None and flood[currentX + 1][currentY] == curVal-1 and East not in mazeWalls[currentCell]:
        return East
    if currentY > 0 and flood[currentX][currentY - 1] != None and flood[currentX][currentY - 1] == curVal-1 and South not in mazeWalls[currentCell]:
        return South
    if currentY < maxWorld and flood[currentX][currentY + 1] != None and flood[currentX][currentY + 1] == curVal-1 and North not in mazeWalls[currentCell]:
        return North

def generate_maze():
    plant(Entities.Bush)
    substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)

def upgradeHarvestTreasure():
    global goal
    if get_entity_type() == Entities.Treasure:
        substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
        if not use_item(Items.Weird_Substance, substance):
            harvest()
            return False
        goal = measure()
        generateFloodFromGoal()
    return True

def generateFloodFromGoal():
    global flood
    global goal
    global mazeWalls
    quick_print("Flood RESET")
    curX = get_pos_x()
    curY = get_pos_y()
    #Flood Updates given certain Walls
    toProcess = [goal]
    while toProcess != []:
        current = toProcess.pop(0)
        procX = current[0]
        procY = current[1]
        currentId = str(procX)+","+str(procY)
        newVal = flood[procX][procY] + 1
        currentWalls = []
        if currentId in mazeWalls:
            currentWalls = mazeWalls[currentId]
        if procY < maxWorld and North not in currentWalls:
            if flood[procX][procY + 1] == None:
                toProcess.append((procX, procY + 1))
                flood[procX][procY + 1] = newVal
        if procY > 0 and South not in currentWalls:
            if flood[procX][procY - 1] == None:
                toProcess.append((procX, procY - 1))
                flood[procX][procY - 1] = newVal
        if procX < maxWorld and East not in currentWalls:
            if  flood[procX + 1][procY] == None:
                toProcess.append((procX + 1, procY))
                flood[procX + 1][procY] = newVal
        if procX > 0 and West not in currentWalls:
            if flood[procX - 1][procY] == None:
                toProcess.append((procX - 1, procY))
                flood[procX - 1][procY] = newVal
        if procX == curX and procY == curY:
            break
    for row in flood:
        quick_print(row)

def updateFloodFromNewestWall():
    global flood
    global lastAddedMazeWalls
    global goal
    global mazeWalls
    curX = get_pos_x()
    curY = get_pos_y()
    quick_print("Flood UPDATE")
    toProcess = []
    midX = (curX + goal[0]) // 2
    midY = (curY + goal[1]) // 2
    toProcess.append((midX, midY))
    while toProcess != []:
        current = toProcess.pop(0)
        procX = current[0]
        procY = current[1]
        currentId = str(procX)+","+str(procY)
        newVal = flood[procX][procY] + 1
        currentWalls = []
        if currentId in mazeWalls:
            currentWalls = mazeWalls[currentId]
        if procY < maxWorld and North not in currentWalls:
            if flood[procX][procY + 1] != newVal:
                toProcess.append((procX, procY + 1))
                flood[procX][procY + 1] = newVal
        if procY > 0 and South not in currentWalls:
            if flood[procX][procY - 1] != newVal:
                toProcess.append((procX, procY - 1))
                flood[procX][procY - 1] = newVal
        if procX < maxWorld and East not in currentWalls:
            if  flood[procX + 1][procY] != newVal:
                toProcess.append((procX + 1, procY))
                flood[procX + 1][procY] = newVal
        if procX > 0 and West not in currentWalls:
            if flood[procX - 1][procY] != newVal:
                toProcess.append((procX - 1, procY))
                flood[procX - 1][procY] = newVal
        if procX == curX and procY == curY:
            break
    for row in flood:
        quick_print(row)

def updateCurrentMaze():
    global mazeWalls
    global lastAddedMazeWalls
    curX = get_pos_x()
    curY = get_pos_y()
    currentCell = (str(curX)+","+str(curY))
    northCell = (str(curX)+","+str(curY + 1))
    southCell = (str(curX)+","+str(curY - 1))
    eastCell = (str(curX + 1)+","+str(curY))
    westCell = (str(curX - 1)+","+str(curY))
    newCurrentCellWall = []
    if currentCell not in mazeWalls:
        mazeWalls[currentCell] = []
    if not can_move(North):
        if North not in newCurrentCellWall:
            newCurrentCellWall.append(North)
        if curY < maxWorld:
            if northCell not in mazeWalls:
                mazeWalls[northCell] = []
            if South not in mazeWalls[northCell]:
                mazeWalls[northCell].append(South)
                lastAddedMazeWalls = [curX, curY + 1]
    if not can_move(South):
        if South not in newCurrentCellWall:
            newCurrentCellWall.append(South)
        if curY > 0:
            if southCell not in mazeWalls:
                mazeWalls[southCell] = []
            if North not in mazeWalls[southCell]:
                mazeWalls[southCell].append(North)
                lastAddedMazeWalls = [curX, curY - 1]
    if not can_move(East):
        if East not in newCurrentCellWall:
            newCurrentCellWall.append(East)
        if curX < maxWorld:
            if eastCell not in mazeWalls:
                mazeWalls[eastCell] = []
            if West not in mazeWalls[eastCell]:
                mazeWalls[eastCell].append(West)
                lastAddedMazeWalls = [curX + 1, curY]
    if not can_move(West):
        if West not in newCurrentCellWall:
            newCurrentCellWall.append(West)
        if curX > 0:
            if westCell not in mazeWalls:
                mazeWalls[westCell] = []
            if East not in mazeWalls[westCell]:
                mazeWalls[westCell].append(East)
                lastAddedMazeWalls = [curX - 1, curY]
    if mazeWalls[currentCell] != newCurrentCellWall:
        mazeWalls[currentCell] = newCurrentCellWall
        # generateFloodFromGoal()

def initializeMaze():
    global flood
    global mazeWalls
    global goal
    flood = []
    for x in range(worldSize):
        flood.append([])
        for y in range(worldSize):
            flood[x].append(None)
    mazeWalls = {}
    clear() #START AT 0,0
    generate_maze()
    goal = measure()
    flood[goal[0]][goal[1]] = 0

def solveMaze():
    global flood
    global mazeWalls
    initializeMaze()
    updateCurrentMaze()
    generateFloodFromGoal()
    while upgradeHarvestTreasure():
        nextDirection = getSortedFloodNeighbors()
        if nextDirection == None or not move(nextDirection):
            # generateFloodFromGoal()
            updateFloodFromNewestWall()
            continue
        updateCurrentMaze()
        # while not can_move(currentNeighbors[0]['direction']):
        #     currentNeighbors = getSortedFloodNeighbors()
        #     updateCurrentMaze()
        #     generateFloodFromGoal()
        # move(currentNeighbors[0]['direction'])
        # if can_move(currentNeighbors[0]['direction']):
        #     move(currentNeighbors[0]['direction'])
        # elif can_move(currentNeighbors[1]['direction']):
        #     move(currentNeighbors[1]['direction'])
        # elif can_move(currentNeighbors[2]['direction']):
        #     move(currentNeighbors[2]['direction'])
        # elif can_move(currentNeighbors[3]['direction']):
        #     move(currentNeighbors[3]['direction'])

if __name__ == "__main__":
    solveMaze()