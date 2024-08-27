# 1514 - Path with Maximum Probability
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        edgeMap = {i: [] for i in range(n)}
        for i, (orig, dest) in enumerate(edges):
            edgeMap[orig].append((dest, succProb[i]))
            edgeMap[dest].append((orig, succProb[i]))

        targetPrbs = [0 for i in range(n)]
        targetPrbs[start_node] = 1
        heap = [(-1,start_node)]
        while heap:
            _,curr = heapq.heappop(heap)
            if curr == end_node:
                return targetPrbs[end_node]
            for to, prob in edgeMap[curr]:
                if prob * targetPrbs[curr] > targetPrbs[to]:
                    targetPrbs[to] = prob * targetPrbs[curr]
                    heapq.heappush(heap,(-targetPrbs[to], to))
            #print(curr, targetPrbs)
        return targetPrbs[end_node]
