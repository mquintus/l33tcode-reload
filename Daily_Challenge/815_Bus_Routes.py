# 815 - Bus Routes
import heapq
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        edges = {}
        for routenr, route in enumerate(routes):
            for orig in route:
                if orig not in edges:
                    edges[orig] = set()
                edges[orig].add(routenr)

        if target not in edges or source not in edges:
            return -1

        print(edges[target], edges[source])

        connectors = {}
        for stop, connections in edges.items():
            for orig in connections:
                if orig not in connectors:
                    connectors[orig] = set()
                for dest in connections:
                    connectors[orig].add(dest)

        visited = {}
        states = []
        for conn in edges[source]:
            states.append((1, conn))

        while len(states) > 0:
            cost, orig = heapq.heappop(states)
            if orig in edges[target]:
                return cost
                
            visited[orig] = True

            for dest in connectors[orig]:
                if dest in visited.keys():
                    continue

                new_cost = cost + 1
                heapq.heappush(states, (new_cost, dest,))
        return -1
        
