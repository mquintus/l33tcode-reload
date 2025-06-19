# 2294 - Partition Array Such That Maximum Difference Is K
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        partitions = 0
        pointer = 0
        while pointer < n and partitions < n:
            #print("Starting at", pointer, "with value", nums[pointer], "to maximize the subarray including numbers up until", nums[pointer]+k, "the next subarray starts at" , bisect.bisect_left(nums, nums[pointer]+k+1), "length",n)
            pointer = bisect.bisect_left(nums, nums[pointer]+k+1)
            partitions += 1
        return partitions
