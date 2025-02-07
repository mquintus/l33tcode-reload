# 3160 - Find the Number of Distinct Colors Among the Balls
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        result = []
        curr = 0
        colorings = {}
        colors = {}
        for loc, col in queries:
            if col not in colors:
                colors[col] = 0
            
            if loc in colorings:
                oldcolor = colorings[loc]
                colors[oldcolor] -= 1
                if colors[oldcolor] == 0:
                    curr -= 1
            else:
                colorings[loc] = 0

            colorings[loc] = col
                
            colors[col] += 1
            if colors[col] == 1:
                curr += 1
            
            result.append(curr)
        return result
