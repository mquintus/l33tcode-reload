# 2311 - Longest Binary Subsequence Less Than or Equal to K
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        while int(s, 2) > k:
            pos = s.index("1")
            s = s[:pos] + s[(pos+1):]
        return len(s)
