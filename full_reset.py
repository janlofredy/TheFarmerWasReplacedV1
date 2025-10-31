from helpers import *
import single_maze
import multi_maze
import multi_pumpkin
import multi_cactus
import cheaty_maze_full

def checkUnlockReq(unlock):
    reqs = get_cost(unlock)
    for item in reqs:
        if num_items(item) < reqs[item]:
            return False
    return True


# SPEED 1/5
while(num_items(Items.Hay) < 20):
    harvest()
unlock(Unlocks.Speed)
# EXPAND 1/9
while(num_items(Items.Hay) < 30):
    if can_harvest():
        harvest()
    move(North)
unlock(Unlocks.Expand)
worldSize = get_world_size()
maxWorld = worldSize-1
# PLANT
while(num_items(Items.Hay) < 50):
    if can_harvest():
        harvest()
    move(North)
unlock(Unlocks.Plant)
# EXPAND 2/9
flyTo(0,1)
while num_items(Items.Wood) < 20:
    if can_harvest():
        harvest()
    plant(Entities.Bush)
unlock(Unlocks.Expand)
worldSize = get_world_size()
maxWorld = worldSize-1
# SPEED 2/5
harvest()
flyTo(1,1)
while num_items(Items.Wood) < 20:
    if can_harvest():
        harvest()
    plant(Entities.Bush)
unlock(Unlocks.Speed)
# CARROTS 1/10
harvest()
flyTo(1,1)
while num_items(Items.Wood) < 50:
    if can_harvest():
        harvest()
    plant(Entities.Bush)
    move(North)
    move(East)
unlock(Unlocks.Carrots)
# WATERING, CARROTS 2/10
while num_items(Items.Wood) < 1750:
    if can_harvest():
        harvest()
    plant(Entities.Bush)
    move(North)
    move(East)
unlock(Unlocks.Watering)
unlock(Unlocks.Carrots)
# HAY 2/10 - 3/10
def plantBushes():
    if can_harvest():
        harvest()
    plant(Entities.Bush)
flyToOrigin()
jobEdge(plantBushes)
while num_items(Items.Hay) < 300:
    if can_harvest():
        harvest()
unlock(Unlocks.Grass)
unlock(Unlocks.Grass)
while num_items(Items.Hay) < 1000:
    if can_harvest():
        harvest()
# TREES 1/10, SUNFLOWERS, SPEED 3/10, EXPAND 3/9
def plantBushHay():
    x,y = getCurrentPos()
    if can_harvest():
        harvest()
    a = (x + y) % 2
    if a == 0:
        plant(Entities.Bush)
    else:
        if get_ground_type() == Grounds.Soil:
            till()
jobEdge(plantBushHay)
flyTo(1,1)
till()
while num_items(Items.Carrot) < 1000:
    if can_harvest():
        harvest()
    plant(Entities.Carrot)
unlock(Unlocks.Trees)
unlock(Unlocks.Sunflowers)
unlock(Unlocks.Speed)
unlock(Unlocks.Expand)
worldSize = get_world_size()
maxWorld = worldSize-1
# FERTILIZER 1/4
def plantHayBush():
    if can_harvest():
        harvest()
    x, y = getCurrentPos()
    a = (x + y) % 2
    if a == 0:
        plant(Entities.Bush)
flyToOrigin()
jobEdge(plantHayBush)
flyTo(1, 1)
lastMove = 0
while num_items(Items.Wood) < 500:
    if can_harvest():
        harvest()
    plant(Entities.Tree)
    move(ALL_DIRECTIONS[lastMove])
    lastMove = (lastMove + 1) % 4
unlock(Unlocks.Fertilizer)
# MAZE 1/6
while num_items(Items.Weird_Substance) < 5000:
    if can_harvest():
        harvest()
    plant(Entities.Tree)
    use_item(Items.Fertilizer)
    move(ALL_DIRECTIONS[lastMove])
    lastMove = (lastMove + 1) % 4
unlock(Unlocks.Mazes)
# MEGAFARM 1/5, 2/5
clear()
while num_items(Items.Gold) < 2000:
    single_maze.startMaze()
unlock(Unlocks.Megafarm)
while num_items(Items.Gold) < 8000:
    multi_maze.startMaze()
unlock(Unlocks.Megafarm)
clear()
# PUMPKIN 1/10
unlock(Unlocks.Pumpkins)
# CACTUS 1/ 10
flyToOrigin()
jobEdge(plantBushHay)
flyTo(1,1)
lastMove = 0
while num_items(Items.Carrot) < 5000:
    if can_harvest():
        harvest()
    x, y = getCurrentPos()
    a = (x + y) % 2
    if a == 0:
        if get_ground_type() != Grounds.Soil:
            till()
        plant(Entities.Carrot)
    move(ALL_DIRECTIONS[lastMove])
    lastMove = (lastMove + 1) % 4
clear()
while num_items(Items.Pumpkin) < 5000:
    multi_pumpkin.collect()
unlock(Unlocks.Cactus)
# DINOSAUR
while num_items(Items.Pumpkin) < 5000:
    multi_pumpkin.collect()
while not checkUnlockReq(Unlocks.Dinosaurs): 
    multi_cactus.collect()
unlock(Unlocks.Dinosaurs)
# FERTILIZER 2 - 4/4, MEGAFARM 3 - 5/5
unlock(Unlocks.Fertilizer)
unlock(Unlocks.Fertilizer)
jobEdge(plantBushHay)
lastMove = 0
flyTo(1,1)
while num_items(Items.Weird_Substance) < 100000:
    if can_harvest():
        harvest()
    plant(Entities.Tree)
    if get_water() <= .75:
        use_item(Items.Water)
    use_item(Items.Fertilizer)
    move(ALL_DIRECTIONS[lastMove])
    lastMove = (lastMove + 1) % 4
unlock(Unlocks.Fertilizer)
while not checkUnlockReq(Unlocks.Megafarm): 
    multi_maze.startMaze()
unlock(Unlocks.Megafarm)
while not checkUnlockReq(Unlocks.Megafarm): 
    multi_maze.startMaze()
unlock(Unlocks.Megafarm)
# LEADERBOARD
jobEdge(plantBushHay)
lastMove = 0
flyTo(1,1)
while num_items(Items.Weird_Substance) < 300000:
    if can_harvest():
        harvest()
    plant(Entities.Tree)
    if get_water() <= .75:
        use_item(Items.Water)
    use_item(Items.Fertilizer)
    move(ALL_DIRECTIONS[lastMove])
    lastMove = (lastMove + 1) % 4
cheaty_maze_full.startMaze()
clear()
while num_items(Items.Pumpkin) < 10000:
    multi_pumpkin.collect()
clear()
multi_cactus.prepare()
while num_items(Items.Cactus) < 12000:
    multi_cactus.collect()
clear()
unlock(Unlocks.Dinosaurs)
unlock(Unlocks.Expand)
unlock(Unlocks.Expand)
multi_cactus.prepare()
while num_items(Items.Cactus) < 100000:
    multi_cactus.collect()
clear()
import snake
while num_items(Items.Bone) < 2000000:
    snake.startSnake()
unlock(Unlocks.Leaderboard)

# # JUST WAIT
# while True:
#     pass