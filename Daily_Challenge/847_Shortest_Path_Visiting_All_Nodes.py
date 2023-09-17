import heapq
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        bestValue = [100000000]

        n = len(graph)

        if n == 1:
            return 0

        statevector = [{} for _ in range(n)]
        states = []

        for start in range(n):
            # start = 0
            visited = 1 << start 
            states.append([0, start, visited])
        
        while len(states) > 0:
            edgeCount, right, visited = heapq.heappop(states)
            
            #print(left, right, visited)
            visitedAll = True
            if visited == (1 << n) - 1:
                return edgeCount

            #for neighbor in graph[left]:
            #    v = visited
            #    v |= (1 << neighbor)
            #    if [neighbor, right, v] in statevector:
            #        continue
            #    statevector.append([neighbor, right, v])
            #    heapq.heappush(states, [edgeCount+1, neighbor, right, v])
            for neighbor in graph[right]:
                v = visited
                v |= (1 << neighbor)
                if v in statevector[neighbor]:
                    continue
                statevector[neighbor][v] = True
                heapq.heappush(states, [edgeCount+1, neighbor, v])

        return bestValue[0]
