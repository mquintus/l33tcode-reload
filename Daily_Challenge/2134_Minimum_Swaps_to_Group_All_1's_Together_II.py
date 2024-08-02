# 2134 - Minimum Swaps to Group All 1's Together II
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        groupSize = sum(nums)
        n = len(nums)

        curr_sum = sum(nums[-groupSize:])
        max_sum = curr_sum
        prev_pos = -groupSize
        for i in range(n):
            curr_sum += nums[i]
            curr_sum -= nums[prev_pos]
            prev_pos += 1
            max_sum = max(max_sum, curr_sum)
        
        return groupSize - max_sum
