class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        splittings = 0
        prev = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            curr = nums[i]
            
            if curr > prev:
                splittings_local = math.ceil(curr / prev)
                splittings += splittings_local - 1
                prev = curr // splittings_local
            else:
                prev = curr
        return splittings


