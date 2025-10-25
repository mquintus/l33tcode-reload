# 1716 - Calculate Money in Leetcode Bank
class Solution:
    def totalMoney(self, n: int) -> int:
        fullweeks = n // 7
        dayofweek = n % 7
        def gauss(x):
            return (x*(x+1))//2
        part1 = gauss(7) * fullweeks
        part2 = 7 * gauss(fullweeks-1) 
        part3 = gauss(dayofweek + fullweeks) 
        part4 = -gauss(fullweeks)
        #print(part1, part2, part3, part4)
        return part1 +  part2 + part3 + part4
