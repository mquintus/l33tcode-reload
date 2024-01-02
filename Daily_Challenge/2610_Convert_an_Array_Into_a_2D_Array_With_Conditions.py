# 2610 - Convert an Array Into a 2D Array With Conditions
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        hashmap = {}
        result = []
        for n in nums:
            pos = 0
            if n not in hashmap:
                hashmap[n] = pos
            else:
                pos = hashmap[n]
            if len(result) <= pos:
                result.append([])
            result[pos].append(n)
            hashmap[n] += 1
        return result
