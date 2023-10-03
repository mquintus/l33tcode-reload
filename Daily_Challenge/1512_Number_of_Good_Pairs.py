# 1512 - Number of Good Pairs
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashTable = {}
        for i in nums:
            if i in hashTable:
                hashTable[i] += 1
            else:
                hashTable[i] = 1

        counter = 0
        for key, val in hashTable.items():
            if val > 1:
                counter += ((val - 1) * (val)) // 2
        return counter
