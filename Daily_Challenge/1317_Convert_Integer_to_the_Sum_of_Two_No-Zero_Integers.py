# 1317 - Convert Integer to the Sum of Two No-Zero Integers
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1,n):
            if -1 == str(a).find('0'):
                b = n - a
                if -1 == str(b).find('0'):
                    return [a,b]
