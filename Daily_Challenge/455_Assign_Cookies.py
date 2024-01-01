# 455 - Assign Cookies
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        happy = 0

        gp = len(g) - 1
        sp = len(s) - 1

        while gp >= 0 and sp >= 0:
            size = s[sp]
            greed = g[gp]
            if size >= greed:
                happy += 1
                sp -= 1

            gp -= 1
        
        return happy

        
