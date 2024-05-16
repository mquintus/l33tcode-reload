# 2812 - Find the Safest Path in a Grid
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        safety_queue = []
        for row_id in range(n):
            for col_id in range(n):
                if grid[row_id][col_id] == 1:
                    safety_queue.append((1, row_id, col_id))

        # Override all zeros with distance to nearest thief
        while safety_queue:
            lowest_safety, row_id, col_id = heapq.heappop(safety_queue)
            nextcells = (
                (row_id+1, col_id),
                (row_id, col_id+1),
                (row_id-1, col_id),
                (row_id, col_id-1),
                )
            for next_row, next_col in nextcells:
                if next_row < 0 or next_col < 0 or next_col >= n or next_row >= n:
                    continue
                if grid[next_row][next_col] != 0:
                    continue
                grid[next_row][next_col] = lowest_safety + 1
                heapq.heappush(safety_queue, (lowest_safety + 1, next_row, next_col))


        # Find best path
        #print(grid)
        position = (-1 * grid[0][0], (0, 0))
        grid[0][0] = 0
        path = [position]
        achieved_safety = -3 * n
        #steps = 0
        while path:
            #steps += 1
            #print(achieved_safety, (row_id, col_id), path)
            lowest_safety, (row_id, col_id) = heapq.heappop(path)
            #if lowest_safety == -2:
            #    print(steps, '---------------------------', lowest_safety, row_id, col_id)
            
            achieved_safety = max(achieved_safety, lowest_safety)

            if row_id == n-1 and col_id == n-1:
                #print("Break")
                break
            nextcells = (
                (row_id+1, col_id),
                (row_id, col_id+1),
                (row_id-1, col_id),
                (row_id, col_id-1),
                )
            for next_row, next_col in nextcells:
                #print("Candidate next steps:", nextcells)
                if next_row < 0 or next_col < 0 or next_col >= n or next_row >= n:
                    #print("Out of bounds", (next_row, next_col))
                    continue
                safety = grid[next_row][next_col]
                if safety == 0:
                    #print("Already visited", (next_row, next_col))
                    continue
                #print("Adding", (next_row, next_col))
                heapq.heappush(path, (safety * -1, (next_row, next_col)))
                grid[next_row][next_col] = 0

        return achieved_safety * -1 - 1
