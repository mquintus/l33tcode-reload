# 3342 - Find Minimum Time to Reach Last Room II
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows = len(moveTime)
        cols = len(moveTime[0])
        states =[ (0, 0,0,1)]
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        while states:
            time,r,c,odd = heapq.heappop(states)
            for dr,dc in directions:
                nc=c+dc
                nr=r+dr
                if nc < 0 or nr < 0 or nc >= cols or nr >= rows:
                    continue
                if moveTime[nr][nc] == -1:
                    continue
                newtime = max(time, moveTime[nr][nc]) + odd
                heapq.heappush(states, (newtime, nr,nc,3-odd))
                moveTime[nr][nc] = -1
                if nr == rows-1 and nc == cols-1:
                    return newtime
