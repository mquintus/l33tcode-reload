import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])

        if n == m == 1:
            return 0

        directions = [[-1,0], [0,-1], [1,0], [0,1]]
        visited = [[False for _ in range(m)] for _ in range(n)]
        efforts = [[10_000_000 for _ in range(m)] for _ in range(n)]
        states = [[0,[m-1,n-1]]]
        while len(states) > 0:
            effort, position = heapq.heappop(states)

            #print(effort, position)
            if position == [0,0]:
                return effort

            visited[position[1]][position[0]] = True

            for next_step in directions:
                x = position[0] + next_step[0]
                y = position[1] + next_step[1]
                if x < 0 or y < 0 or x >= m or y >= n:
                    continue
                if visited[y][x]:
                    continue
                next_effort = max(effort, abs(heights[y][x] - heights[position[1]][position[0]]))
                if efforts[y][x] > next_effort:
                    efforts[y][x] = next_effort
                    heapq.heappush(states, [next_effort,[x,y]])
            
        return 0
