# 1481 - Least Number of Unique Integers after K Removals
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        c = sorted(c.values())
        different_numbers = len(c)
        for el in c:
            if k >= el:
                different_numbers -= 1
                k -= el
        return different_numbers
