# 1458 - Max Dot Product of Two Subsequences
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[False for _ in range(len(nums2) + 2)] for _ in range(len(nums1) + 2)]

        dp[len(nums1) - 1][len(nums2) - 1] = nums1[-1] * nums2[-1]

        def solve(i,j):
            if dp[i][j] != False:
                return dp[i][j]
            
            if i == len(nums1):
                return -1000000
            if j == len(nums2):
                return -1000000
            
            take = (nums1[i] * nums2[j])
            if take > 0:
                take = max(take, take + solve(i+1, j+1))
            skip1 = solve(i + 1, j)
            skip2 = solve(i, j + 1)

            dp[i][j] = max(take, skip1, skip2)
            return dp[i][j]

        return solve(0,0)
