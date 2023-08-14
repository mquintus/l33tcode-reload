class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        This can be solved without sorting the whole array

        but some basic sorting is necessary.

        There is an algorithm that works with two pointers
        and sorts an individual element to its position.
        While all other elements left left or right from it
        and are "sorted" only in being larger or smaller than
        the pivot element.
        '''


        def quickselect(nums, k):
            pivot = len(nums) // 2 
            left = []
            right = []
            mid = 0

            for i in nums:
                if i < nums[pivot]:
                    left.append(i)
                elif i > nums[pivot]:
                    right.append(i)
                else:
                    mid += 1

            if len(right) >= k:
                return quickselect(right, k)
            
            if len(right) + mid < k:
                return quickselect(left, k - len(right) - mid)
            
            return nums[pivot]
        return quickselect(nums, k)
