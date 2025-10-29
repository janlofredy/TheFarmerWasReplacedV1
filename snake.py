# ASSUME WORLD SIZE IS MULTIPLES OF 2
# set_world_size(10)
# clear()
change_hat(Hats.Straw_Hat)
while get_pos_x() > 0:
    move(West)
while get_pos_y() > 0:
    move(South)
change_hat(Hats.Dinosaur_Hat)
face = North
tail = 1
change_hat(Hats.Dinosaur_Hat)
appleX, appleY = measure()
area = get_world_size() ** 2

DIRS = [North, South, East, West]
DIR_VECTORS = {
    North: (0, 1),
    South: (0, -1),
    East:  (1, 0),
    West:  (-1, 0)
}
prepDip = get_world_size() - 2
firstDipLength = (get_world_size() * 4) - prepDip - 4

def moveCheckAndSetApple(direction):
    global appleX
    global appleY
    global tail
    move(direction)
    if get_entity_type() == Entities.Apple:
        appleX, appleY = measure()
        tail += 1
        if (get_world_size() ** 2) - 1 == tail:
            # print("WE WIN", tail)
            move(North)
            move(South)
            move(East)
            move(West)
            change_hat(Hats.Straw_Hat)
            tail = 1
            change_hat(Hats.Dinosaur_Hat)
            appleX, appleY = measure()

def dip(prep= False, col = 1, depth = prepDip):
    global prepDip
    global tail
    if col == 0 or col == get_world_size()-1:
        return
    if depth == 0 or depth == get_world_size()-1:
        return
    colSet = col
    if col % 2 == 0:
        colSet -= 1
    while get_pos_x() < colSet:
        moveCheckAndSetApple(East)
    if tail > (get_world_size() ** 2) // 2:
        depth = prepDip
    for _ in range(depth):
        moveCheckAndSetApple(South)
    moveCheckAndSetApple(East)
    for _ in range(depth):
        moveCheckAndSetApple(North)
    moveCheckAndSetApple(East)
    if not prep and appleX >= get_pos_x():
            dip(False, appleX, prepDip - appleY + 1)

def custom_ceil(x):
    int_part = int(x)  # Truncate decimal
    if x > 0 and x != int_part:
        return int_part + 1
    else:
        return int_part

def reset():
    while get_pos_x() < get_world_size()-1:
        moveCheckAndSetApple(East)
    while get_pos_y() > 0:
        moveCheckAndSetApple(South)
    while get_pos_x() > 0:
        moveCheckAndSetApple(West)
    while get_pos_y() < get_world_size()-1:
        moveCheckAndSetApple(North)
    moveCheckAndSetApple(East)

    dipsRequired = (tail - firstDipLength) // (prepDip * 2)
    if (tail - firstDipLength) % (prepDip * 2) != 0:
        dipsRequired += 1
    for col in range(dipsRequired):
        dip(True, (col+1)*2)

moveCheckAndSetApple(North)
for _ in range(prepDip):
    moveCheckAndSetApple(North)
moveCheckAndSetApple(East)
while True:
    if num_items(Items.Bone) >= 33488928:
        break
    dip(False, appleX, prepDip - appleY + 1)
    reset()