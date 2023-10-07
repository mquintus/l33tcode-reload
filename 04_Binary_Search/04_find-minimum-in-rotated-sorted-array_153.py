class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def findRotationBinarySearch(nums: List[int]) -> int:
            start = 0
            end = len(nums)

            if nums[start] < nums[end - 1]:
                return 0

            while end > start:
                mid = (start + end) // 2

                if mid == len(nums) - 1:
                    end -= 1
                    mid -= 1
                
                if nums[mid] > nums[mid + 1]:
                    return mid + 1

                if nums[start] < nums[mid]:
                    start = mid
                elif nums[end - 1] > nums[mid]:
                    end = mid
                else:
                    return mid

        r = findRotationBinarySearch(nums)

        return nums[r]
