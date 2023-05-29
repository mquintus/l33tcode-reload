class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Naive solution:
        Pop an element from the list and search for the "complement" in the remaining list.
        Time complexity: O(n^2)
        Space complexity: O(1) - we are only ever storing two counters.
        '''
        def naive_solution(nums: List[int], target: int) -> List[int]:
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if target - nums[i] == nums[j]:
                        return i,j
        return naive_solution(nums, target)
