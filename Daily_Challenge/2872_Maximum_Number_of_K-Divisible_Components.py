# 2872 - Maximum Number of K-Divisible Components
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        neighbors = [[] for _ in range(n)]
        for f,t in edges:
            for a,b in [[f,t],[t,f]]:
                neighbors[a].append(b)
        
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)
        

        # print("leaves",leaves)
        # print("neighbors",neighbors)
        componentcount = 1
        while len(leaves):
            node = leaves.pop()
            
            neighbor = neighbors[node][0]
            if values[node] % k != 0:
                values[neighbor] += values[node]
                values[neighbor] %= k
            else:
                componentcount += 1
                
            neighbors[node] = []
            neighbors[neighbor].remove(node)
            
            if len(neighbors[neighbor]) == 1:
                leaves.append(neighbor)
            if len(neighbors[neighbor]) == 0:
                leaves.remove(neighbor)

            
        return componentcount


