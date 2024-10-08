# 1963 - Minimum Number of Swaps to Make the String Balanced
class Solution:
    def minSwaps(self, s: str) -> int:
        left = 0
        right = len(s)-1
        r = 0
        c = 0
        while left < right:
            if s[left] == "]":
                if c == 0: 
                    r += 1
                    c = 1
                    while s[right] != '[':
                        right -= 1
                    right -= 1
                else:
                    c -= 1
            else:
                c += 1
            left += 1
        return r
