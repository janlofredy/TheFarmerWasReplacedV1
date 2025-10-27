from helpers import *
def solveMaze():
    goal = measure()
    worldMap = {}
    worldMap[getCurrentPos()] = getCurrentNeighbors()
    while getCurrentPos() != goal:
        neighbors = getCurrentNeighbors()
        worldMap[getCurrentPos()] = neighbors

def reconstructPath():
    path = []
    return path

def getCurrentNeighbors():
    neighbors = []
    if can_move(North):
        neighbors.append({'x': get_pos_x(), 'y': get_pos_y() + 1, 'direction': North})
    if can_move(South):
        neighbors.append({'x': get_pos_x(), 'y': get_pos_y() - 1, 'direction': South})
    if can_move(East):
        neighbors.append({'x': get_pos_x() + 1, 'y': get_pos_y(), 'direction': East})
    if can_move(West):
        neighbors.append({'x': get_pos_x() - 1, 'y': get_pos_y(), 'direction': West})
    return neighbors


if __name__ == "__main__":
    solveMaze()