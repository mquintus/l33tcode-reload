# 2045 - Second Minimum Time to Reach Destination
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        visited_once = {}
        visited_twice = set()
        edges = [(a-1,b-1) for a,b in edges]
        trans = [[] for _ in range(n)]
        for orig, dest in edges:
            trans[orig].append(dest)
            trans[dest].append(orig)

        state = [0, 0]
        states = deque()
        states.append(state)
        while states:
            location, cost = states.popleft()

            delay = 0
            next_reset_time = (2*change)
            point_in_time = cost % next_reset_time
            if point_in_time >= change:
                delay = next_reset_time - point_in_time

            for dest in trans[location]:
                newcost = cost+time+delay
                if dest in visited_twice or (dest in visited_once and visited_once[dest] >= newcost):
                    #print(dest, "in visited_twice")
                    continue

                state = [dest, newcost]
                if dest not in visited_once:
                    visited_once[dest] = newcost
                elif dest in visited_once:
                    visited_twice.add(dest)
                    if dest == n-1:
                        return newcost

                #print(state)
                states.append(state)

        return 0
