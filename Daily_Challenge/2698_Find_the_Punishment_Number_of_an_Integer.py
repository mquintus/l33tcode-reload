# 2698 - Find the Punishment Number of an Integer
class Solution:
    def punishmentNumber(self, n: int) -> int:
        sol = [1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 235, 297, 369, 370, 379, 414, 657, 675, 703, 756, 792, 909, 918, 945, 964, 990, 991, 999, 1000]
        p = bisect.bisect_right(sol, n)
        return sum([i**2 for i in sol[:p]])
