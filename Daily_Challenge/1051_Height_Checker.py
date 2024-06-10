# 1051 - Height Checker
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        hsorted = sorted(heights)
        c = 0
        for i in range(len(heights)):
            if hsorted[i] != heights[i]:
                c+=1
        return c
