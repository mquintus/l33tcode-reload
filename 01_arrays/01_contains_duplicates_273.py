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
        # return iterative(nums)

        '''
        Alternative idea: 
        Recursive approach to pop the first element and check if it still in the list,
        otherwise recursively do the check on the remaining (popped) list.
        Time complexity: O(n^2)
        Space complexity: O(1)
        but worse by a constant factor to handle the recursive context change.
        '''
        def recursive(nums: List[int]) -> bool:
            if len(nums) == 0:
                return False
            first = nums.pop()
            if first in nums:
                return True
            return recursive(nums)
        return recursive(nums)
