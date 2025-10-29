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
        droneJob()
    spawn_drone(dronePositionRight) # Spawning of 2nd Drone
    for hPos in range(half-1): # Spawned by 1st Drone half-1 times
        def dronePosition():
            for _ in range(half - hPos - 1):
                move(East)
            droneJob()
        spawn_drone(dronePosition)
    droneJob()
def testJob():
    return None

spawnDronesFastest(testJob)