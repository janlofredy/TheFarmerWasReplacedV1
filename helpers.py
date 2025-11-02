# ALL_HATS = [
#     # Hats.Dinosaur_Hat, # dont wear for fun. only one hat owned
#     Hats.Brown_Hat,
#     Hats.Cactus_Hat,
#     Hats.Carrot_Hat,
#     Hats.Gold_Hat,
#     # Hats.Gold_Trophy_Hat,
#     Hats.Golden_Cactus_Hat,
#     Hats.Golden_Carrot_Hat,
#     Hats.Golden_Gold_Hat,
#     Hats.Golden_Pumpkin_Hat,
#     Hats.Golden_Sunflower_Hat,
#     Hats.Golden_Tree_Hat,
#     Hats.Gray_Hat,
#     Hats.Green_Hat,
#     Hats.Pumpkin_Hat,
#     Hats.Purple_Hat,
#     # Hats.Silver_Trophy_Hat,
#     Hats.Straw_Hat,
#     Hats.Sunflower_Hat,
#     Hats.The_Farmers_Remains,
#     Hats.Top_Hat,
#     Hats.Traffic_Cone,
#     Hats.Traffic_Cone_Stack,
#     Hats.Tree_Hat,
#     Hats.Wizard_Hat,
#     # Hats.Wood_Trophy_Hat
# ]
ALL_HATS = [Hats.Straw_Hat]
ALL_DIRECTIONS = [North, East, South, West]
worldSize = get_world_size()
maxWorld = worldSize-1

def flyToOrigin():
    flyTo(0,0)
def longFlyToY(y):
    while(get_pos_y() < y):
        move(North)
    while(get_pos_y() > y):
        move(South)
def longFlyToX(x):
    while(get_pos_x() < x):
        move(East)
    while(get_pos_x() > x):
        move(West)
def longFlyTo(x, y):
    while(get_pos_x() < x):
        move(East)
    while(get_pos_x() > x):
        move(West)
    while(get_pos_y() < y):
        move(North)
    while(get_pos_y() > y):
        move(South)

def flyTo(x, y):
    flytoY(y)
    flyToX(x)

def flyToX(xPos):
    goRight = True
    distX = xPos - get_pos_x()
    if(get_pos_x() > xPos):
        goRight = False
        distX = get_pos_x() - xPos
    if(distX > get_world_size()/2):
        goRight = not goRight
    if(goRight):
        while(get_pos_x() != xPos):
            move(East)
    else:
        while(get_pos_x() != xPos):
            move(West)
def flytoY(yPos):
    goUp = True
    distY = yPos - get_pos_y()
    if(get_pos_y() > yPos):
        goUp = False
        distY = get_pos_y() - yPos
    if(distY > get_world_size()/2):
        goUp = not goUp
    if(goUp):
        while(get_pos_y() != yPos):
            move(North)
    else:
        while(get_pos_y() != yPos):
            move(South)

def jobEverywhere(job):
    flyToOrigin()
    for _x in range(get_world_size()):
        for _y in range(get_world_size(), 0, -1):
            job()
            move(East)
        move(South)

def jobEdge(job):
    worldSize = get_world_size()
    maxWorld = worldSize-1
    # 0, 0
    flyToOrigin() 
    # 0, maxWorld
    while get_pos_y() < maxWorld:
        job()
        move(North)
    # maxWorld, maxWorld
    while get_pos_x() < maxWorld:
        job()
        move(East)
    # maxWorld, 0
    while get_pos_y() > 0:
        job()
        move(South)
    # 0, 0
    while get_pos_x() > 0:
        job()
        move(West)

def jobDownwards(job):
    for _y in range(get_world_size()):
        job()
        move(South)
def jobUpwards(job):
    for _y in range(get_world_size()):
        job()
        move(North)

def jobRightwards(job):
    for _x in range(get_world_size()):
        job()
        move(East)

# TILL ONLY JOB = 3.27 seconds
def spawnDronesSimultaneously(droneJob):
    # set_world_size(max_drones()//2)
    top = get_world_size() -1
    half = get_world_size()//2
    flyTo(0, 0) # Assumed at Game's WORLD ORIGIN
    for col in range(get_world_size()//2):
        def dronePositionRight():
            for i in range(half-col-1):
                move(West)
            droneJob()
        def dronePositionLeft():
            for i in range(half-col):
                move(East)
            droneJob()
        drone = spawn_drone(dronePositionLeft)
        drone = spawn_drone(dronePositionRight)
    droneJob()
    # return drones
# TILL ONLY JOB = 3.27 seconds
def spawnDronesSimultaneouslyFun(droneJob):
    # set_world_size(max_drones())
    top = get_world_size() -1
    drones = []
    # flyTo(0, top)
    for col in range(top):
        def dronePosition():
            change_hat(ALL_HATS[col % len(ALL_HATS)])
            for i in range(top-col):
                move(East)
            droneJob()
        # drones.append(spawn_drone(dronePosition))
        drone = spawn_drone(dronePosition)
        if drone:
            drones.append(drone)
        else:
            change_hat(ALL_HATS[col % len(ALL_HATS)])
    change_hat(ALL_HATS[0 % len(ALL_HATS)])
    change_hat(ALL_HATS[0 % len(ALL_HATS)])
    droneJob()
    return drones

# TILL ONLY JOB = 4.2 seconds
def spawnDronesLine(droneJob, orientation = "horizontal"):
    drones = []
    size = get_world_size() - 1
    # ASSUMED GRID IS AUTO RESETTED
    if orientation == "horizontal":
        for _col in range(size):
            drones.append(spawn_drone(droneJob))
            move(East)
        droneJob()
    else:
        for _row in range(size):
            drones.append(spawn_drone(droneJob))
            move(North)
        droneJob()
    return drones

# TILL ONLY JOB = 2.78 seconds
def spawnDronesQuarters(droneJob, orientation = "horizontal"):
    half = worldSize // 2
    quarter = worldSize // 4
    # ASSUMED STARTING AT 0,0
    for _ in range(quarter):
        move(East)
    def droneRightSpawner():
        # for _ in range(quarter):
        #     move(West)
        def droneQuarterLeftSpawner():
            for qMoves in range(quarter-1):
                def dronePositionQuarters():
                    for _ in range(quarter-qMoves):
                        move(West)
                    droneJob()
                spawn_drone(dronePositionQuarters)
            move(West)
            droneJob()
        spawn_drone(droneQuarterLeftSpawner)
        for qMoves in range(quarter-1):
            def dronePositionQuarters():
                for _ in range(quarter-qMoves-1):
                    move(East)
                droneJob()
            spawn_drone(dronePositionQuarters)
        droneJob()
    spawn_drone(droneRightSpawner)
    move(North)
    # for _ in range(quarter - 1):
    #     move(East)
    def droneQuarterRightSpawner():
        for qMoves in range(quarter-1):
            def dronePositionQuarters():
                for _ in range(quarter-qMoves):
                    move(East)
                droneJob()
            spawn_drone(dronePositionQuarters)
        move(East)
        droneJob()
    spawn_drone(droneQuarterRightSpawner)
    for qMoves in range(quarter-1):
        def dronePositionQuarters():
            for _ in range(quarter-qMoves-1):
                move(West)
            droneJob()
        spawn_drone(dronePositionQuarters)
    droneJob() # FOR THE CHILD DRONES

# TILL ONLY JOB = 2.75 seconds
def spawnDronesFastest(droneJob):
    half = 32//2
    def dronePositionRight(): #2nd Drone
        move(West)
        for hPos in range(half-1): # Spawned By 2nd Drone half-1 times
            def dronePosition():
                for _ in range(half-hPos-1):
                    move(West)
                droneJob()
            spawn_drone(dronePosition)
        # change_hat(Hats.Straw_Hat)
        # change_hat(Hats.Straw_Hat)
        droneJob()
    spawn_drone(dronePositionRight) # Spawning of 2nd Drone
    # change_hat(Hats.Straw_Hat)
    for hPos in range(half-1): # Spawned by 1st Drone half-1 times
        def dronePosition():
            for _ in range(half - hPos - 1):
                move(East)
            droneJob()
        spawn_drone(dronePosition)
    droneJob()
# TILL ONLY JOB = 2.75 seconds
def spawnDronesFastestVertical(droneJob):
    half = 32//2
    def dronePositionUp(): #2nd Drone
        move(North)
        for hPos in range(half-1): # Spawned By 2nd Drone half-1 times
            def dronePosition():
                for _ in range(half-hPos-1):
                    move(North)
                droneJob()
            spawn_drone(dronePosition)
        # change_hat(Hats.Straw_Hat)
        # change_hat(Hats.Straw_Hat)
        droneJob()
    spawn_drone(dronePositionUp) # Spawning of 2nd Drone
    # change_hat(Hats.Straw_Hat)
    for hPos in range(half-1): # Spawned by 1st Drone half-1 times
        def dronePosition():
            for _ in range(half - hPos - 1):
                move(South)
            droneJob()
        spawn_drone(dronePosition)
    droneJob()

def spawnDroneRecursive():
    # def callRecursive():
    #     return spawnDroneRecursive(droneJob)
    while num_drones() < max_drones():
        spawn_drone(spawnDroneRecursive)
    # return droneJob()

def getCurrentPos():
    return (get_pos_x(), get_pos_y())

def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def infiniteWait():
    while True:
        # do_a_flip()
        pass
def testJob():
    pass
    # print(num_drones())
    # do_a_flip()
    # jobUpwards(till)
    return None

if __name__ == "__main__":
    # clear()
    # for i in range(16):
    #     change_hat(Hats.Straw_Hat)
    # spawnDronesLine(testJob)
    # spawnDronesSimultaneously(testJob)
    # spawnDronesSimultaneouslyFun(testJob) 
    spawnDronesQuarters(infiniteWait)
    # spawnDronesFastest(testJob) 
    # spawnDroneRecursive(testJob)
    # spawnDroneRecursive()
    # print(num_drones())
    # till()
    # move(North)
    # till()
    # plant(Entities.Cactus)
    # print(measure())
    # print(measure(South))
    # swap(South)
    # for i in range((worldSize//4) -1):
    #     move(East)
