# 2971 - Find Polygon With the Largest Perimeter
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Condition: The sum of the other sides has to be larger than the largest part.
        # 1. Sort 
        nums.sort()
        # 2. Iterate all edges, keep running sum, identify largest possible option
        running = 0
        count = 0
        max_index = -1
        running_max = -1
        for i, edge in enumerate(nums):
            if i >= 2:
                if running > edge:
                    max_index = i
                    running_max = running + edge
            running += edge
            
        return running_max




