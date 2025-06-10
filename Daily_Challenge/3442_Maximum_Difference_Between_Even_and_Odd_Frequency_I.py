# 3442 - Maximum Difference Between Even and Odd Frequency I
class Solution:
    def maxDifference(self, s: str) -> int:
        evenmin = float('inf')
        oddmax = -1

        for i in range(26):
            l = chr(ord('a')+i)
            f = s.count(l)
            if f == 0:
                continue
            if f%2 == 0:
                evenmin = min(evenmin, f)
            else:
                oddmax = max(oddmax, f)

        return oddmax-evenmin
