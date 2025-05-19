# 3024 - Type of Triangle
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0] + nums[1] <= nums[2] or nums[0] + nums[2] <= nums[1] or  nums[1] + nums[2] <= nums[0]:
            t = "none"
        elif nums[0] == nums[1] and nums[0] == nums[2]:
            t = "equilateral"
        elif nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
            t = "isosceles"
        else:
            t = "scalene"
        return t
