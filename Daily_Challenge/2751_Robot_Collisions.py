# 2751 - Robot Collisions
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # A version of "asteroids"

        # sort by position
        ids = [i for i in range(len(positions))]
        ids = [x for _, x in sorted(zip(positions, ids))]
        healths = [x for _, x in sorted(zip(positions, healths))]
        directions = [x for _, x in sorted(zip(positions, directions))]

        robots = [[directions[i],healths[i],ids[i]] for i in range(len(positions))]

        survivors = []
        stack = []

        #print(robots)
        for direction, health, index in robots:
            if direction == 'R':
                stack.append([health, index])
                continue
            elif direction == 'L':
                while len(stack) > 0:
                    if health > stack[-1][0]:
                        stack.pop()
                        health -= 1
                    elif health == stack[-1][0]:
                        stack.pop()
                        health = 0
                        break
                    elif health < stack[-1][0]:
                        stack[-1][0] -= 1
                        health = 0
                        break
                if health == 0:
                    continue
                if len(stack) == 0:
                    survivors.append([health, index])
            

        survivors.extend(stack)
        survivors = [[index, health] for health, index in survivors]
        survivors.sort()
        survivors = [health for index, health in survivors]

        return survivors
