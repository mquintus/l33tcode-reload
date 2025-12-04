# 2211 - Count Collisions on a Road
class Solution:
    def countCollisions(self, directions: str) -> int:
        collisions = 0
        right = 0
        still = False
        for d in directions:
            if d == "R": 
                right += 1

            elif d == "S":
                collisions += right
                right = 0
                still = True

            elif d in "L":
                if right > 0:
                    collisions += right
                    right = 0
                    still = True

                if still:
                    collisions += 1

        return collisions
