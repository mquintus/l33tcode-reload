# 1304 - Find N Unique Integers Sum up to Zero
class Solution:
    def sumZero(self, n: int) -> List[int]:
        return list(range(2,2*n,2)) + [-n*(n-1)]
