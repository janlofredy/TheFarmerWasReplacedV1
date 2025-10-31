sizeSet = 4
dronesMax = sizeSet * sizeSet

# For the "Recycling" and "Big Gold Farmer" achievements
def generate_maze():
    plant(Entities.Bush)
    substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)


def maze():
    while num_items(Items.Gold) < 1000000:
        if num_drones() == dronesMax:
            if get_entity_type() == Entities.Treasure:
                substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
                if not use_item(Items.Weird_Substance, substance):
                    harvest()
                # harvest()
            generate_maze()

def startMaze():
    clear()
    filledPos = []
    while num_drones() < dronesMax:
        pos_x = get_pos_x()
        pos_y = get_pos_y()
        current = (pos_x, pos_y)
        if current not in filledPos:
            filledPos.append(current)
            spawn_drone(maze)
            move(North)
        else:
            move(East)
    maze()

if __name__ == "__main__":
    clear()
    set_world_size(sizeSet)
