# 3243 - Shortest Distance After Road Addition Queries I
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        prev_dist = []
        seq=[[i+1] for i in range(0,n-1)]
        seq.append([])
        
        for i in range(0,n):
            prev_dist.append(i)
        
        #BFS
        def update(orig):
            states = [orig]
            while states:
                pos = states.pop(0)
                for follower in seq[pos]:
                    if prev_dist[follower] > prev_dist[pos] + 1:
                        prev_dist[follower] = prev_dist[pos] + 1
                        states.append(follower)

        solution = []
        for orig, dest in queries:
            # Add new edge
            seq[orig].append(dest)
            new_dist = prev_dist[orig] + 1
            if prev_dist[dest] > new_dist:
                prev_dist[dest] = new_dist
                update(dest)
            # Distance is stored in our list
            solution.append(prev_dist[n-1])
        return solution
