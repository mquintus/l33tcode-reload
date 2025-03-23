# 1976 - Number of Ways to Arrive at Destination
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        edges = {i:[] for i in range(n)}
        for f,g,c in roads:
            edges[f].append((g,c))
            edges[g].append((f,c))

        MOD = 1_000_000_007

        visited = [False] * n
        states = [(0,0)]
        shortest_distance = [float("inf")] * n
        shortest_distance[0] = 0
        globally_shortest = float("inf")
        count = [0] * n
        count[0] = 1
        #print(edges)
        while states:
            c_prev,f = heapq.heappop(states)
            if visited[f]: continue
            visited[f] = True
            #print(f"Visiting node {f} at time {c_prev} with already {count[f]} ways" )
            if c_prev > globally_shortest:
                continue
            for g,c in edges[f]:
                new_distance = c + shortest_distance[f]
                if new_distance > shortest_distance[g] or new_distance > globally_shortest:
                    continue
                if g == n-1:
                    globally_shortest = new_distance
                    #print(f"Global minimum: {globally_shortest}")
                else:
                    heapq.heappush(states, (new_distance,g))
                if new_distance < shortest_distance[g]:
                    shortest_distance[g] = new_distance
                    count[g] = 0
                count[g] = (count[g] + count[f])  % MOD
                #print(f"node {f} -> {g} at time {new_distance} adds up to {count[g]} ways" )
        return count[n-1] % MOD






