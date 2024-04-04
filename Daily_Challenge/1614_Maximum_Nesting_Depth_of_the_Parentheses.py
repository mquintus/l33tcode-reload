# 1614 - Maximum Nesting Depth of the Parentheses
class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        mdepth = 0
        for el in s:
            if el == '(':
                depth += 1
                mdepth = max(mdepth, depth)
            elif el == ')':
                depth -= 1
        return mdepth
