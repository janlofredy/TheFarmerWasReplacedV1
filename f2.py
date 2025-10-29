TOTAL = 32

def drone0(): 
    droneLoop(0)
def drone1(): 
    droneLoop(1)
def drone2(): 
    droneLoop(2)
def drone3(): 
    droneLoop(3)
def drone4(): 
    droneLoop(4)
def drone5(): 
    droneLoop(5)
def drone6(): 
    droneLoop(6)
def drone7(): 
    droneLoop(7)
def drone8(): 
    droneLoop(8)
def drone9(): 
    droneLoop(9)
def drone10(): 
    droneLoop(10)
def drone11(): 
    droneLoop(11)
def drone12(): 
    droneLoop(12)
def drone13(): 
    droneLoop(13)
def drone14(): 
    droneLoop(14)
def drone15(): 
    droneLoop(15)
def drone16(): 
    droneLoop(16)
def drone17(): 
    droneLoop(17)
def drone18(): 
    droneLoop(18)
def drone19(): 
    droneLoop(19)
def drone20(): 
    droneLoop(20)
def drone21(): 
    droneLoop(21)
def drone22(): 
    droneLoop(22)
def drone23(): 
    droneLoop(23)
def drone24(): 
    droneLoop(24)
def drone25(): 
    droneLoop(25)
def drone26(): 
    droneLoop(26)
def drone27(): 
    droneLoop(27)
def drone28(): 
    droneLoop(28)
def drone29(): 
    droneLoop(29)
def drone30(): 
    droneLoop(30)
def drone31(): 
    droneLoop(31)

droneFunctions = [
    drone0, drone1, drone2, drone3, drone4, drone5, drone6, drone7,
    drone8, drone9, drone10, drone11, drone12, drone13, drone14, drone15,
    drone16, drone17, drone18, drone19, drone20, drone21, drone22, drone23,
    drone24, drone25, drone26, drone27, drone28, drone29, drone30, drone31
]
def spawnDrones3Tree():
    spawn_drone(droneFunctions[0])  # Start with root drone
    
def droneLoop(index):
    target = index  # Final position in line

    # Move first to avoid congestion
    while get_pos_x() != target:
        if get_pos_x() < target:
            move(East)
        else:
            move(West)

    # Spawn up to 3 children
    child1 = 3 * index + 1
    child2 = 3 * index + 2
    child3 = 3 * index + 3

    if child1 < TOTAL:
        spawn_drone(droneFunctions[child1])
    if child2 < TOTAL:
        spawn_drone(droneFunctions[child2])
    if child3 < TOTAL:
        spawn_drone(droneFunctions[child3])
        
spawnDrones3Tree()