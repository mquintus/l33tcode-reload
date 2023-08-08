class Solution:
    def search(self, nums: List[int], target: int) -> int:
        overflow = False
        
        start = 0
        end = len(nums)
        mid = 0
        while start < end:
            mid = (start + end ) // 2
            if nums[mid] > nums[- 1]:
                start = mid + 1
            elif nums[mid] <= nums[- 1]:
                end = mid
        mid = (start + end ) // 2
        pivot = mid


        start = 0
        end = len(nums)
        mid = 0
        while overflow == False or start < end:
            mid = (start + end ) // 2

            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
            
            if overflow == False:
                if end < 1:
                    start = pivot
                    end = len(nums)
                    overflow = True
                elif start == end:
                    start = 0
                    end = pivot
                    overflow = True

        return -1
                
