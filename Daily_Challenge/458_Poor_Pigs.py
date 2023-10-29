# 458 - Poor Pigs
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        rounds = minutesToTest//minutesToDie + 1
        pigs = 0
        while rounds ** pigs < buckets:
            pigs += 1
        return pigs
