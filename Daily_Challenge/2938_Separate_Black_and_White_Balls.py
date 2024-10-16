# 2938 - Separate Black and White Balls
class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        distance = 0
        count = 0

        for char in s:
            if char == "0":
                distance += count
            else:
                count += 1
        
        return distance

