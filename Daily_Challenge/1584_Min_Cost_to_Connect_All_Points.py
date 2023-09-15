import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        connected = [False] * 1001

        distances = []

        def get_distance(p1,p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        unConnectedNodes = len(points)

        first_node = points[0]
        min_dist = 0
        for i, node in enumerate(points):
            d = get_distance(first_node, node)
            heapq.heappush(distances, (d, node, i,))

        while len(distances) > 0:
            travel, next_node, node_id = heapq.heappop(distances)
            # print(next_node, node_id)
            if connected[node_id]:
                continue
            connected[node_id] = True
            min_dist += travel
            unConnectedNodes -= 1
            if unConnectedNodes == 0:
                break

            for i, node in enumerate(points):
                if connected[i]:
                    continue
                d = get_distance(next_node, node)
                heapq.heappush(distances, (d, node, i,))

        return min_dist
