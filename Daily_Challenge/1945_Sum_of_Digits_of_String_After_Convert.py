# 1945 - Sum of Digits of String After Convert
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        dsum = ""
        a = ord('a')
        for c in s:
            dsum += str(ord(c) - a + 1)
        
        def digitsum(s):
            dsum = 0
            for c in s:
                dsum += int(c)
            return dsum

        for _ in range(k):
            dsum = str(digitsum(dsum))

        return int(dsum)
