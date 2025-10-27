DIRS = [North, South, East, West]
DIR_VECTORS = {
    North: (0, -1),
    South: (0, 1),
    East:  (1, 0),
    West:  (-1, 0)
}

MAX_COST = 999999

def get(d, key, default):
    if key in d:
        return d[key]
    return default

def sort_queue(queue):
    i = 0
    while i < len(queue) - 1:
        j = i + 1
        while j < len(queue):
            a = queue[i][0]
            b = queue[j][0]
            if a[0] > b[0] or (a[0] == b[0] and a[1] > b[1]):
                temp = queue[i]
                queue[i] = queue[j]
                queue[j] = temp
            j += 1
        i += 1

def push(queue, priority, item):
    queue.append((priority, item))
    sort_queue(queue)

def pop(queue):
    if len(queue) == 0:
        return None
    return queue.pop(0)

def remove(queue, item):
    i = 0
    while i < len(queue):
        if queue[i][1] == item:
            queue.pop(i)
            return
        i += 1

def heuristic(x1, y1, x2, y2):
    dx = x1 - x2
    if dx < 0:
        dx = -dx
    dy = y1 - y2
    if dy < 0:
        dy = -dy
    return dx + dy

def key(u, g, rhs, start, km):
    gx = get(g, u, MAX_COST)
    rx = get(rhs, u, MAX_COST)
    if gx < rx:
        min_g_rhs = gx
    else:
        min_g_rhs = rx
    h = heuristic(start[0], start[1], u[0], u[1])
    return (min_g_rhs + h + km, min_g_rhs)

def update_vertex(u, g, rhs, open_list, goal, km, start, get_successors):
    if u[0] != goal[0] or u[1] != goal[1]:
        min_rhs = MAX_COST
        neighbors = get_successors(u)
        i = 0
        while i < len(neighbors):
            s = neighbors[i]
            cost = get(g, s, MAX_COST) + 1
            if cost < min_rhs:
                min_rhs = cost
            i += 1
        rhs[u] = min_rhs
    remove(open_list, u)
    gx = get(g, u, MAX_COST)
    rx = get(rhs, u, MAX_COST)
    if gx != rx:
        push(open_list, key(u, g, rhs, start, km), u)

def compute_shortest_path(g, rhs, open_list, start, goal, km, get_successors):
    while True:
        if len(open_list) == 0:
            break
        top_key, u = open_list[0]
        k_start = key(start, g, rhs, start, km)
        if top_key[0] > k_start[0] or (top_key[0] == k_start[0] and top_key[1] > k_start[1]):
            pass
        elif get(rhs, start, MAX_COST) == get(g, start, MAX_COST):
            break
        pop(open_list)
        if get(g, u, MAX_COST) > get(rhs, u, MAX_COST):
            g[u] = rhs[u]
            neighbors = get_successors(u)
            i = 0
            while i < len(neighbors):
                update_vertex(neighbors[i], g, rhs, open_list, goal, km, start, get_successors)
                i += 1
        else:
            g[u] = MAX_COST
            update_vertex(u, g, rhs, open_list, goal, km, start, get_successors)
            neighbors = get_successors(u)
            i = 0
            while i < len(neighbors):
                update_vertex(neighbors[i], g, rhs, open_list, goal, km, start, get_successors)
                i += 1

# Main D* Lite function — online flow
def dstar_lite(start, goal, can_move, move):
    g = {}
    rhs = {}
    open_list = []
    km = 0
    known_directions = {}
    current = start

    def explore(pos):
        if pos in known_directions:
            return
        directions = []
        i = 0
        while i < 4:
            d = DIRS[i]
            if can_move(d):
                directions.append(d)
            i += 1
        known_directions[pos] = directions

    def get_successors(pos):
        if pos not in known_directions:
            return []
        x = pos[0]
        y = pos[1]
        directions = known_directions[pos]
        successors = []
        i = 0
        while i < len(directions):
            d = directions[i]
            dx = DIR_VECTORS[d][0]
            dy = DIR_VECTORS[d][1]
            neighbor = (x + dx, y + dy)
            if neighbor in known_directions:
                successors.append(neighbor)
            i += 1
        return successors

    rhs[goal] = 0
    push(open_list, key(goal, g, rhs, current, km), goal)
    explore(current)
    compute_shortest_path(g, rhs, open_list, current, goal, km, get_successors)

    path = [current]
    while current[0] != goal[0] or current[1] != goal[1]:
        directions = known_directions[current]
        min_cost = MAX_COST
        next_step = None
        i = 0
        while i < len(directions):
            d = directions[i]
            dx = DIR_VECTORS[d][0]
            dy = DIR_VECTORS[d][1]
            neighbor = (current[0] + dx, current[1] + dy)
            if neighbor in known_directions:
                cost = get(g, neighbor, MAX_COST)
                if cost < min_cost:
                    min_cost = cost
                    next_step = (neighbor, d)
            i += 1
        if next_step == None:
            break
        current = next_step[0]
        direction = next_step[1]
        move(direction)
        explore(current)
        path.append(current)
        compute_shortest_path(g, rhs, open_list, current, goal, km, get_successors)

    return path

dstar_lite((get_pos_x(), get_pos_y()), measure(), can_move, move)