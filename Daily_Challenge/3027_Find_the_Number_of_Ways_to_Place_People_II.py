# 3027 - Find the Number of Ways to Place People II
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        count = 0
        points.sort(key=lambda x: (x[0], -x[1]))
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                if points[i][1] >= points[j][1]:
                    for k in range(i+1, j):
                        if points[k][1] >= points[j][1] and points[k][1] <= points[i][1]:
                            break
                    else:
                        count += 1
        return count
