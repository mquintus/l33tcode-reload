# 976 - Largest Perimeter Triangle
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        n = len(nums)
        for i in range(n-1,1,-1):
            first = nums[i]
            # print("////////////",  first)
            for j in range(i-1, 0,-1):
                second = nums[j]
                # print(second)
                minimal = first - second + 1
                maximal = first + second - 1
                
                # print(first, second, maximal, bisect.bisect_right(nums, maximal) )
                k = bisect.bisect_left(nums, maximal) 
                if k == -1: break
                if k >= j: 
                    k = j - 1
                newthird = nums[k]
                if newthird > maximal:
                    break
                if newthird < minimal:
                    break
                # print("At position",k,"we find satisfying value",newthird)
                return first+second+newthird
        return 0


                    
