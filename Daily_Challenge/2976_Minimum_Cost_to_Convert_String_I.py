# 2976 - Minimum Cost to Convert String I
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = 26
        distances = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            distances[i][i] = 0
        #edges = [[] for _ in range(n)]
        #usedletters = set(source) | set(target)
        a = ord('a')
        for i in range(len(original)):
            orig = ord(original[i]) - a
            dest = ord(changed[i]) - a
            if distances[orig][dest] > cost[i]:
                distances[orig][dest] = cost[i]
        
        for waypoint in range(n):
            for orig in range(n):
                if distances[orig][waypoint] == float('inf'):
                    continue
                for dest in range(n):
                    c = distances[waypoint][dest]
                    #print(distances[orig][dest])
                    if distances[orig][dest] > distances[orig][waypoint] + c:
                        distances[orig][dest] = distances[orig][waypoint] + c
        
        sumcost = 0
        for i in range(len(source)):
            orig = ord(source[i]) - a
            dest = ord(target[i]) - a
            sumcost += distances[orig][dest]

        if sumcost == float('inf'):
            return -1
        return sumcost
