# 1493 - Longest Subarray of 1's After Deleting One Element
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero = 0
        n = len(nums)
        c = nums.count(0)
        if c == 0 or c == 1: return n - 1

        left = 0
        right = -1
        solution = 0
        while left < n:
            right += 1
            if right < n and nums[right] == 0:
                zero += 1

            if right >= n: break
            while left < n and zero >= 2 and left < right:
                if nums[left] == 0:
                    zero -= 1
                left += 1
     
            localsolution = right - left - zero + 1
            #print(zero, (right, left, ), localsolution)
            solution = max(solution, localsolution)
        localsolution = right - left - zero 
        #print(zero, (right, left, ), localsolution)
        solution = max(solution, localsolution)
        
        return solution
            

