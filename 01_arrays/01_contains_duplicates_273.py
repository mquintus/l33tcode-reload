class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        Naive idea: 
        Take the first element and check if it is still in the list.
        otherwise iterate to the next element and check if it is in the right part of the list.
        Time complexity: O(n^2)
        Space complexity: O(1)
        '''
        def iterative(nums: List[int]) -> bool:
            for pos, val in enumerate(nums):
                print(pos, val)
                if val in nums[pos+1:]:
                    return True
            return False
        return iterative(nums)
