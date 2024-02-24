# 2092 - Find All People With Secret
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        knowing = set()
        knowing.add(0)
        knowing.add(firstPerson)

        edges = {}
        for orig, dest, time in meetings:
            if orig not in edges:
                edges[orig] = []
            edges[orig].append([time, dest])
            if dest not in edges:
                edges[dest] = []
            edges[dest].append([time, orig])

        states = [[0,0], [0,firstPerson]]
        while states:
            time, person = heapq.heappop(states)
            knowing.add(person)

            if person not in edges:
                continue

            for weight, following in edges[person]:
                if following in knowing:
                    continue
                if weight < time:
                    continue
                state = [weight, following]
                #print(state)
                heapq.heappush(states, state)

        return list(knowing)
