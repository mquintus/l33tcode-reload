# 264 - Ugly Number II
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        visited = set()
        pipe = [1]
        for i in range(n):
            curr = heapq.heappop(pipe)
            if len(pipe) < n:
                for m in [2,3,5]:
                    nexxt = curr*m
                    if nexxt not in visited:
                        heapq.heappush(pipe, nexxt)
                        visited.add(nexxt)
            #pipe.sort()
            #print(pipe)
        return curr
