class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        success = 0
        max_success = 0
        buildings = [0 for i in range(n)]
        states = [(0, buildings, success)]
        while len(states) > 0:
            i, buildings, success = states.pop()
            if i == len(requests):
                balance = True
                for b in buildings:
                    if b != 0:
                        balance = False
                        break
                if balance:
                    max_success = max(max_success, success)
                continue

            orig = requests[i][0]
            dest = requests[i][1]
            for action in ['allow', 'deny']:
                # deny   -> never deny self-assignment
                if action == 'deny' and orig != dest:
                    states.append([i+1, buildings, success])
                if action == 'allow':
                    myb = buildings.copy()
                    #print(requests, i, len(requests))
                    myb[orig] -= 1
                    myb[dest] += 1
                    states.append([i+1, myb, success+1])

        return max_success
