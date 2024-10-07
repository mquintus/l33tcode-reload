# 2696 - Minimum String Length After Removing Substrings
class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for char in s:
            if len(stack) > 0 and (char == 'B' and stack[-1] == 'A' or char == 'D' and stack[-1] == 'C'):
                stack.pop()
            else:
                stack.append(char)
        return len(stack)
