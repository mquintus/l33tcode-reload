class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connections_per_city = [0] * n
        connected = [[False] * n for _ in range(n)]

        for r in roads:
            a,b = sorted(r)
            connections_per_city[a] += 1
            connections_per_city[b] += 1
            connected[a][b] = True
            connected[b][a] = True

        max_val = -1
        max_val_2 = -1
        for c in range(n):
            if connections_per_city[c] > max_val:
                max_val_2 = max_val
                max_val = connections_per_city[c]
            elif connections_per_city[c] > max_val_2:
                max_val_2 = connections_per_city[c]

        best_connected = []
        second_best_connected = []
        for c in range(n):
            if connections_per_city[c] == max_val:
                best_connected.append(c)
            if connections_per_city[c] == max_val_2:
                second_best_connected.append(c)

        has_two = False
        for c in best_connected:
            for d in best_connected:
                if c != d:
                    has_two = True
                    if not connected[c][d]:
                        return max_val + max_val
        if has_two:
            return max_val + max_val - 1
        
        for c in best_connected:
            for d in second_best_connected:
                if not connected[c][d]:
                    return max_val + max_val_2

        return max_val + max_val_2 - 1

