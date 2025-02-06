# 1726 - Tuple with Same Product
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        if len(nums) < 4: return 0
        # if a solution is found, multiply by 8
        hashmap = {}

        result = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                prod = nums[i] * nums[j] 
                if prod not in hashmap:
                    hashmap[prod] = 1
                else:
                    result += 8*hashmap[prod]
                    hashmap[prod] += 1
                    
        
        return result
