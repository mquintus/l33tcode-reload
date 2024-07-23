# 1636 - Sort Array by Increasing Frequency
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = sorted([(x,-y) for y,x in Counter(nums).items()])
        full = []
        for count, val in counts:
            full += [-val] * count
        return full
