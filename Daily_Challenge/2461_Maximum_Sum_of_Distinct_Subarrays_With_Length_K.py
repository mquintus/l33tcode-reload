# 2461 - Maximum Sum of Distinct Subarrays With Length K
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = 10**5 + 1
        nn = len(nums)
        currsum = sum(nums[:k])
        maxsum = 0
        duplicates = 0
        counts = [0] * n
        for el in nums[:k]:
            counts[el] += 1
            if counts[el] == 2:
                duplicates += 1
        #print(counts, duplicates, maxsum)
        for i in range(0, nn-k):
            if duplicates == 0:
                maxsum = max(currsum, maxsum)           
            el = nums[i]
            currsum -= el
            counts[el] -= 1
            if counts[el] == 1:
                duplicates -= 1
            el = nums[i+k]
            currsum += el
            counts[el] += 1
            if counts[el] == 2:
                duplicates += 1
            #print(counts, duplicates, maxsum)

        if duplicates == 0:
            maxsum = max(currsum, maxsum)
        return maxsum
