# 2894 - Divisible and Non-divisible Sums Difference
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        rangesum = (n*(n+1))//2
        if m == 1:
            return -rangesum
        divisible = 0
        for i in range(m, n+1, m):
            divisible += i
        nondivisible = rangesum - divisible
        return nondivisible - divisible
