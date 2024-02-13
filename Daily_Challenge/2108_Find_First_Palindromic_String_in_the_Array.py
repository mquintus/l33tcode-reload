# 2108 - Find First Palindromic String in the Array
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_p(s):
            if len(s) == 1:
                return True
            p1 = 0
            p2 = len(s) - 1
            while p1 <= p2 and p2 > 0 and p1 < len(s) and s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
            return p1 > p2
        
        for s in words:
            if is_p(s):
                return s
        return ""
