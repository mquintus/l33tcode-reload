# 34 - Find First and Last Position of Element in Sorted Array
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        def binarySearch(start, end, target):
            mid = len(nums) // 2
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    start = mid + 1
                if nums[mid] > target:
                    end = mid - 1
            return mid
        
        is_it_there = binarySearch(0, len(nums) - 1, target)
        if nums[is_it_there] != target:
            return [-1, -1]

        if nums[0] == target:
            start_position = 0
        else:
            start_position = binarySearch(0, is_it_there - 1, target - .5) 
            if nums[start_position] < target:
                start_position += 1
    
        if nums[-1] == target:
            end_position = len(nums) - 1
        else:
            end_position = binarySearch(is_it_there + 1, len(nums) - 1, target + .5)
            print(end_position)
            if nums[end_position] > target:
                end_position -= 1

        return [start_position, end_position]

            
