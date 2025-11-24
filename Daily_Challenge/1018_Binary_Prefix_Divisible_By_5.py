# 1018 - Binary Prefix Divisible By 5
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = len(nums)
        number = 0
        result = []
        for i in range(n):
            number += nums[i]
            #print(number)
            result.append(number % 5 == 0)
            number *= 2
        return result
