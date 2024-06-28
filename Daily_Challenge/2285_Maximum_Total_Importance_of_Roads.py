# 2285 - Maximum Total Importance of Roads
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        for f, t in roads:
            degree[f] += 1
            degree[t] += 1
        degree.sort()
        fullscore = 0
        for points, multiplier in enumerate(degree):
            fullscore += (points+1) * multiplier
        return fullscore
