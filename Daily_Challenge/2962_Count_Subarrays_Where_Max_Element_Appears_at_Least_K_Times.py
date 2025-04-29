# 2962 - Count Subarrays Where Max Element Appears at Least K Times
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxel = max(nums)
        n = len(nums)
        
        maxelcount = 0
        for el in nums:
            if el == maxel:
                maxelcount += 1

        if maxelcount < k:
            return 0

        result = 0
        elcount = 0
        p1 = 0
        p2 = -1
        while p2 <= n:

            while elcount < k:
                p2 += 1
                if p2 >= n: break
                if nums[p2] == maxel:
                    elcount += 1
            if p2 >= n: break
            #print("Solution:",p1,"to",p2)
                
            while elcount >= k:
                if nums[p1] == maxel:
                    elcount -= 1
                p1 += 1

                new = n - p2
                result += new
                #print(p1,p2,new,result)
                if p1 == n: break

        return result
