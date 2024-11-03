# 796 - Rotate String
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        if n != len(goal): return False
        if Counter(s) != Counter(goal): return False
        for pivot in range(n):
            #print(pivot, s[pivot:], goal[:n-pivot], ".", s[:pivot],goal[n-pivot:])
            if s[pivot:] == goal[:n-pivot] and s[:pivot] == goal[n-pivot:]:
                return True
        return False
