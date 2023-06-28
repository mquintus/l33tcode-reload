class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        def approach_with_maxheap(n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
            new_edges = {}
            for i, e in enumerate(edges):
                if not e[0] in new_edges.keys():
                    new_edges[e[0]] = []    
                if not e[1] in new_edges.keys():
                    new_edges[e[1]] = []    
                new_edges[e[0]].append((e[1], succProb[i], i,))
                new_edges[e[1]].append((e[0], succProb[i], i,))


            probabilities = [0 for i in range(n)]
            probabilities[start] = 1
            nodes_to_visit_bfs = [(-1, start,)]
            
            while len(nodes_to_visit_bfs) > 0:
                oldprob, curr_node = heapq.heappop(nodes_to_visit_bfs)
                oldprob = abs(oldprob)

                if curr_node == end:
                    return probabilities[end]

                if curr_node not in new_edges.keys():
                    continue

                for next_node, edge_prob, i in new_edges[curr_node]:
                    next_prob = edge_prob * oldprob
                    if next_prob <= probabilities[next_node]:
                        continue
                    probabilities[next_node] = max(next_prob, probabilities[next_node])
                    
                    heapq.heappush(nodes_to_visit_bfs, (-next_prob, next_node,) )

            return probabilities[end]
            
        return approach_with_maxheap(n, edges, succProb, start, end)
