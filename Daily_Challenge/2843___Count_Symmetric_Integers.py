# 2843 -   Count Symmetric Integers
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        final = 0
        for i in range(low, high+1):
            num = str(i)
            strle = len(num)
            if strle % 2 == 1:
                continue
            half1 = [int(j) for j in num[:strle//2]]
            half2 = [int(j) for j in num[strle//2:]]
            if sum(half1) == sum(half2):
                final += 1
        return final
