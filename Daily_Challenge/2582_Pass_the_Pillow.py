# 2582 - Pass the Pillow
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time = time % (2 * (n-1))
        solution = 1 + time
        if time > n-1:
            solution = 2 * n - time - 1
        return solution
