ALL_HATS = [
    # Hats.Dinosaur_Hat, # dont wear for fun. only one hat owned
    Hats.Brown_Hat,
    Hats.Cactus_Hat,
    Hats.Carrot_Hat,
    Hats.Gold_Hat,
    # Hats.Gold_Trophy_Hat,
    Hats.Golden_Cactus_Hat,
    Hats.Golden_Carrot_Hat,
    Hats.Golden_Gold_Hat,
    Hats.Golden_Pumpkin_Hat,
    Hats.Golden_Sunflower_Hat,
    Hats.Golden_Tree_Hat,
    Hats.Gray_Hat,
    Hats.Green_Hat,
    Hats.Pumpkin_Hat,
    Hats.Purple_Hat,
    # Hats.Silver_Trophy_Hat,
    Hats.Straw_Hat,
    Hats.Sunflower_Hat,
    Hats.The_Farmers_Remains,
    Hats.Top_Hat,
    Hats.Traffic_Cone,
    Hats.Traffic_Cone_Stack,
    Hats.Tree_Hat,
    Hats.Wizard_Hat,
    # Hats.Wood_Trophy_Hat
]
ALL_HATS = [Hats.Straw_Hat]

def flyToOrigin():
    flyTo(0,get_world_size()-1)
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
    flyTo(0, get_world_size()-1)
    for _x in range(get_world_size()):
        for _y in range(get_world_size(), 0, -1):
            job()
            move(East)
        move(South)

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

def spawnDronesSimultaneously(droneJob):
    # set_world_size(max_drones()//2)
    top = get_world_size() -1
    half = get_world_size()//2
    drones = []
    flyTo(0, top)
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
        if drone:
            drones.append(drone)
        drone = spawn_drone(dronePositionRight)
        if drone:
            drones.append(drone)
    droneJob()
    return drones
def spawnDronesSimultaneouslyFun(droneJob):
    # set_world_size(max_drones())
    top = get_world_size() -1
    drones = []
    flyTo(0, 0)
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

def spawnDronesFast(droneJob):
    dronesSpawned = []
    def droneLeftSpawner():
        for _ in range(32):
            move(East)
        droneJob()
    def droneRightSpawner():
        for _ in range(32):
            move(West)
        droneJob()
    
    dronesSpawned.append(spawn_drone(droneJob))
    droneJob() # FOR THE CHILD DRONES
    return dronesSpawned

def getCurrentPos():
    return (get_pos_x(), get_pos_y())

def infiniteWait():
    while True:
        # do_a_flip()
        pass
def testJob():
    jobUpwards(till)

if __name__ == "__main__":
    clear()
    # for i in range(16):
    #     change_hat(Hats.Straw_Hat)
    # spawnDronesFast(infiniteWait,32)
    # spawnDronesLine(testJob)
    # spawnDronesSimultaneously(testJob)
    # spawnDronesSimultaneouslyFun(testJob)
    # print(num_drones())
    till()
    move(North)
    till()
    plant(Entities.Cactus)
    print(measure())
    print(measure(South))
    swap(South)

