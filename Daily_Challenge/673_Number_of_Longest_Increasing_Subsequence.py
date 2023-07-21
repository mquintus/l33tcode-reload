class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        longest = [0 for i in range(len(nums))]

        def longestSubsequence(i):
            if longest[i] != 0:
                return
            
            dp[i] = 1
            longest[i] = 1

            for j in range(i):
                if nums[j] < nums[i]:
                    longestSubsequence(j)
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        longest[i] = 0
                    if dp[j] + 1 == dp[i]:
                        longest[i] += longest[j]
                    
        max_length = 0
        for i in range(len(nums)):
            longestSubsequence(i)
            max_length = max(max_length, dp[i])

        max_count = 0
        for i in range(len(nums)):
            if dp[i] == max_length:
                max_count += longest[i]

        return max_count
