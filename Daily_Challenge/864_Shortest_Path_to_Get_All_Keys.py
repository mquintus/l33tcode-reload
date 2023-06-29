import heapq
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        keys = {} # name, coordinates
        locks = {} # name, coordinates       
        start = None


        def populate_variables():
            for y, row in enumerate(grid):
                for x, cell in enumerate(row):
                    if cell == '@':
                        start = (x,y,)
                    elif cell in 'abcdefghijklmnopqrstuvwxyz':
                        keys[cell] = (x,y,)
                    elif cell in 'abcdefghijklmnopqrstuvwxyz'.upper():
                        locks[cell] = (x,y,)
            return start, keys, locks
                
        start, keys, locks = populate_variables()

        def replace_grid_field(grid, x, y, char):
            grid[y] = grid[y][:x] + char + grid[y][x + 1:]

        replace_grid_field(grid, start[0], start[1], '.')

        def get_heuristic(position, to_key):
            next_key_coords = keys[to_key]
            
            heuristic = abs(position[0] - next_key_coords[0]) + abs(position[1] - next_key_coords[1])
            return heuristic


        def get_possible_directions(grid, position, k, has_keys):
            #print("position", position)
            positions = []
            for p in [
                (position[0] - 1, position[1]),
                (position[0] + 1, position[1]),
                (position[0], position[1] - 1),
                (position[0], position[1] + 1),
                ]:
                if p[0] >= 0 and p[1] >= 0 and p[0] < len(grid[0]) and p[1] < len(grid):
                    cell_value = grid[p[1]][p[0]]
#                    print(p, cell_value)
                    if cell_value == '#':
                        continue
                    if cell_value == cell_value.upper() and cell_value.lower() in has_keys:
                        positions.append(p)
                    if cell_value == k:
                        return [p]
                    if cell_value == '.':
                        positions.append(p)

            return positions


        def getShortestPathFromKeyAToKeyB(position: tuple, to_key: int, has_keys: list) -> int:
            grid_copy = [cell for cell in [row for row in grid]]
            # heuristic, steps, coordinates
            waypoints = [( 10000, 0, position)]
            steps = 0
            while len(waypoints) > 0:
                next_step = heapq.heappop(waypoints)
#                print("Substate:", next_step)
                p = next_step[2]
                steps = next_step[1]
#               print("if grid[p[1]][p[0]] == keys[to_key]:", grid[p[1]][p[0]], keys[to_key])
                if grid[p[1]][p[0]] == to_key:
                    return steps
                steps = steps + 1
                replace_grid_field(grid_copy, p[0], p[1], '@')
                for next_field in get_possible_directions(grid_copy, p, k, has_keys):
#                    print("next_field", next_field)
                    heuristic = get_heuristic(next_field, to_key)
                    heap_el = (heuristic, steps, next_field,)
                    heapq.heappush(waypoints, heap_el)
            return -1

        prev_key = -1
        level_stepcount = 0
        has_keys = []
        states = [ (len(has_keys), level_stepcount, start, has_keys,) ]
        while len(states) > 0:
            state = heapq.heappop(states)
#            print("State:", state)
            has_keys = state[3]
            level_stepcount = state[1]
            curr_pos = state[2]
            if len(has_keys) == len(keys):
                return level_stepcount
            for k in keys.keys():
                if k not in has_keys:
                    distance = getShortestPathFromKeyAToKeyB(curr_pos, k, has_keys)
#                    print("Key:",k, "Distance:", distance)
                    if distance == -1:
                        continue
                    else:                        
                        heapq.heappush(states, 
                                        ( len(has_keys) + 1, 
                                        distance + level_stepcount,
                                        keys[k],
                                        [*has_keys, k], ))

        return -1


