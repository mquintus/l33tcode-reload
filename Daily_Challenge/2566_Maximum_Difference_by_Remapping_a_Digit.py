# 2566 - Maximum Difference by Remapping a Digit
class Solution:
    def minMaxDifference(self, num: int) -> int:
        n = str(num)
        highest = []
        lowest = []
        reph = -1
        repm = -1
        for el in n:
            if int(el) < 9 and reph == -1:
                reph = el
            if int(el) > 0 and repm == -1:
                repm = el
            h = el
            if el == reph:
                h = "9"
            highest.append(h)
            m = el
            if el == repm:
                m = "0"
            lowest.append(m)
        highest = int("".join(highest))
        lowest = int("".join(lowest))
        return highest - lowest
