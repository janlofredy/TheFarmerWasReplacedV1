import single_till
import single_harvest_grid
import single_wood
import single_carrot
import single_pumpkin
import single_sunflower
import single_cactus
import single_maze
from helpers import *

def main():
    while True:
        do_a_flip()
        single_wood.prepare()
        jobEverywhere(single_wood.plantHayAndTree)
        single_carrot.prepare()
        single_carrot.collectCarrots()
        single_harvest_grid.run()
        single_pumpkin.collectPumpkins()
        single_sunflower.collectSunflowers()
        single_cactus.collectCactus()
        single_maze.prepare()
        single_maze.startMaze()
        pet_the_piggy()

if __name__ == "__main__":
    print(max_drones(), get_world_size())
    main()
    # harvest()