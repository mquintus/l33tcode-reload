# 752 - Open the Lock
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def distance(start, target):
            d = 0
            for position in [0,1,2,3]:
                s = int(start[position])
                t = int(target[position])
                dx = min([s+10 - t, abs(s - t),t+10-s])
                d += dx
            return d
        
        visited = set()
        initial_position = "0000"
        myQueue = [(0, distance(initial_position, target), initial_position)]
        visited.add(initial_position)
        while myQueue:
            steps, dist, pos = heapq.heappop(myQueue)
            if dist == 0:
                return steps
            for p in range(4):
                for dx in [-1, 1]:
                    combination = pos[:p] + str((int(pos[p]) + dx) % 10) + pos[p+1:]
                    if combination in deadends or combination in visited:
                        continue
                    visited.add(combination)
                    heapq.heappush(myQueue,
                        [steps+1,distance(combination, target),combination])
        return -1
