# 921 - Minimum Add to Make Parentheses Valid
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = 0
        broken = 0
        for char in s:
            if char == '(':
                left += 1
            else:
                if left == 0:
                    broken += 1
                else:
                    left -= 1
        return broken + left
