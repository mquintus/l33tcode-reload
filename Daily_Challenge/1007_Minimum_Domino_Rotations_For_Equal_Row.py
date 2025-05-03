# 1007 - Minimum Domino Rotations For Equal Row
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        solution = float('inf')
        for a,b in [(tops, bottoms), (bottoms, tops)]:
            for target in [a[0], b[0]]:
                switches_a = 0
                switches_b = 0
                for i in range(n):
                    if a[i] == target:
                        switches_b += 1
                        continue
                    if b[i] == target:
                        switches_a += 1
                        continue
                    break
                else:
                    solution = min(solution, min(switches_a, switches_b))
        if solution == float('inf'):
            return -1
        return solution
