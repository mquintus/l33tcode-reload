# 2206 - Divide Array Into Equal Pairs
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counts = [0] * 501
        uneven = 0
        for el in nums:
            counts[el] = 1 - (counts[el] % 2)
            if counts[el] != 0:
                uneven += 1
            else:
                uneven -= 1
        
        return uneven == 0
