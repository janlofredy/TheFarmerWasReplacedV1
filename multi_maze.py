from helpers import *

def prepare():
    clear()
def buyMaxMaze():
    plant(Entities.Bush)
    substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)
def startMaze():
    for i in range(max_drones()):
        spawnDronesSimultaneously(solveMazeHandOnWallRule)
def solveMazeHandOnWallRule():
    buyMaxMaze()
    direction = [North]
    lastXY = [get_pos_x(), get_pos_y()]
    move(East)
    while(get_entity_type() != Entities.Treasure):
        if measure() == None:
            buyMaxMaze()
        lastMove = direction.pop()
        move(lastMove)
        if(len(direction) == 0):
            direction.append(North)
        if(lastXY[0] == get_pos_x() and lastXY[1] == get_pos_y()):
            direction.append(lastMove)
            if(direction[len(direction)-1] == North):
                direction.append(East)
            elif(direction[len(direction)-1] == East):
                direction.append(South)
            elif(direction[len(direction)-1] == South):
                direction.append(West)
            elif(direction[len(direction)-1] == West):
                direction.append(North)
        lastXY = [get_pos_x(), get_pos_y()]
        # TO LOOP INFINITELY
        # if get_entity_type() == Entities.Treasure:
        #     harvest()
    harvest()

def mainLoop():
    prepare()
    for i in range(9999):
        startMaze()
    # pass


if __name__ == "__main__":
    # solveMazeDStarLiteAlgorithm()
    # solveMazeHandOnWallRule()
    mainLoop()
    # print(can_move(North))