# 525 - Contiguous Array
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        
        balance = [0]
        for el in nums:
            diff = -1
            if el == 1:
                diff = 1
            balance.append(balance[-1] + diff)

        hashmap_earliest = {}
        longest = 0
        for i, b in enumerate(balance):
            if b not in hashmap_earliest:
                hashmap_earliest[b] = i
            else:
                longest = max(longest, i - hashmap_earliest[b])
        return longest
