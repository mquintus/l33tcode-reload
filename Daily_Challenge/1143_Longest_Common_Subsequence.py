# 1143 - Longest Common Subsequence
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1] * len(text2) for _ in range(len(text1))]

        def lss(i,j):
            if i >= n:
                return 0
            if j >= m:
                return 0
            
            if dp[i][j] >= 0:
                return dp[i][j]
            
            if text1[i] == text2[j]:
                dp[i][j] = 1 + lss(i+1,j+1)
            else:
                dp[i][j] = max(lss(i+1,j),lss(i,j+1))
            
            return dp[i][j]
        
        return lss(0,0)
