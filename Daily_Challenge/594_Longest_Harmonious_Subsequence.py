# 594 - Longest Harmonious Subsequence
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        p1 = 0
        p2 = 0
        
        mini = nums[0]
        maxi = nums[0]

        maxlength = 0

        while p1 < n and p2 < n:
            if p1 > p2:
                p2 = p1
                mani = nums[p2]
                maxi = nums[p2]

            diff = maxi-mini
            if diff == 1:
                maxlength = max(maxlength, p2-p1+1)

            if diff <= 1:
                p2 += 1
                if p2 >= n:
                    break
                maxi = nums[p2]
                continue

            if diff > 1:
                p1 += 1
                mini = nums[p1]
                continue
        
        return maxlength
