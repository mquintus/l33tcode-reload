# 2145 - Count the Hidden Sequences
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        start = 0
        down = 0
        up = 0
        for el in differences:
            start += el
            up = max(up, start)
            down = min(down, start)
        width = up - down
        maxwidth = upper - lower
        if maxwidth < width: return 0
        return maxwidth - width + 1
