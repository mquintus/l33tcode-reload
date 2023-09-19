# 287 - Find the Duplicate Number
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Let's say that there is a list with numbers 0...n with n+1 elements
        # because one of the numbers is a duplicate.
        #
        # Mathematically speaking, without duplicates, we can use the gaussian formula
        # to have an estimate value 
        # and then all duplicates are offsetting this estimate value.
        #
        # HOWEVER these restrictions are not for this challenge.
        # Actually, the only restriction is that the highest number can't be larger 
        # than the length of the array.
        #
        n = len(nums) + 1
        hashmap = [False] * n
        for i in nums:
            if hashmap[i] == True:
                return i
            hashmap[i] = True
        return -1

