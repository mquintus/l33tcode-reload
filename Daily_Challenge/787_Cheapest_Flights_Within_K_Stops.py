# 787 - Cheapest Flights Within K Stops
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        routes = {}
        for source, destination, cost in flights:
            if source not in routes:
                routes[source] = []
            routes[source].append([cost, destination])
            routes[source].sort()

        visited = {}
        start_state = [0, 0, src]
        states = [start_state]
        while states:
            #print(states)
            spent, steps, location = heapq.heappop(states)
            visited[location] = [spent, steps]
            if location == dst:
                return spent
            if steps > k:
                continue
            
            if location in routes:
                for travelprice, destination in routes[location]:
                    newprice = spent + travelprice
                    if destination not in visited or visited[destination][0] > newprice or visited[destination][1] > steps:
                        heapq.heappush(states, [newprice, steps + 1, destination])

            
        return -1
