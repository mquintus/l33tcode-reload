# 3075 - Maximize Happiness of Selected Children
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        value = 0
        value += happiness[-1]
        k -= 1
        reduction = 1
        while k > 0:
            curr_value = happiness[-1 - reduction] - reduction
            if curr_value <= 0:
                return value
            value += curr_value
            reduction += 1
            k -= 1
        return value
