# 3152 - Special Array II
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefixXor = nums[0]%2
        special = [0]
        for i, el in enumerate(nums[1:]):
            #print(prefixXor, el%2)
            if el%2 == prefixXor:
                special.append(i+1)
            else:
                special.append(special[-1])
            prefixXor = el%2
        
        #print(special)
        result = []
        for fr, to in queries:
            result.append(special[to] <= fr)

        return result
