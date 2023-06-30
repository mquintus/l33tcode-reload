import collections

class Solution:
    def shortestPathAllKeys(self, grid):
        n = len(grid)
        m = len(grid[0])
        abs_keycount = 0
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == '@':
                    start = (x,y,)
                elif cell in 'abcdefghijklmnopqrstuvwxyz':
                    abs_keycount += 1
                
        
        visited = set()
        walk_dirs = [[0,1],[1,0],[-1,0],[0,-1]]

        keyCount = 0
        #grid_copy = [cell for cell in [row for row in grid]]
        # steps, coordinates
        waypoints = collections.deque()
        waypoints.append( (0, start, "".join(sorted(".@abcdef")), 0,))
        steps = 0
        state_counter = 0
        while waypoints:
            state_counter += 1
            next_step = waypoints.popleft()
            steps = next_step[0]
            p = next_step[1]
            has_keys = next_step[2]
            keyCount = next_step[3]
            steps = next_step[0]
            cell = grid[p[1]][p[0]]
            if cell in 'abcdef' and cell.upper() not in has_keys:
                has_keys += cell.upper()
                has_keys = "".join(sorted(has_keys))
                #print(has_keys, keyCount)
                keyCount += 1
                if keyCount == abs_keycount:
                    print(state_counter)
                    return steps

            #replace_grid_field(grid_copy, p[0], p[1], '@')
            for direction in walk_dirs:
                x = p[0] + direction[0]
                y = p[1] + direction[1]
                if x >= 0 and y >= 0 and x < m and y < n:
                    if grid[y][x] in has_keys:
                        if (x, y, has_keys,) not in visited:
                            heap_el = [steps + 1, (x, y,) , has_keys, keyCount]
                            waypoints.append(heap_el)
                            visited.add((x, y, has_keys,))
        print(state_counter)
        return -1
