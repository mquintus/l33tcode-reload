# 2762 - Continuous Subarrays
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        p0 = 0
        p1 = 0

        upper = nums[p0]
        lower = nums[p0]
        valuecounts = {}

        cont = True
        count = 0
        while p1 < n:
            #print(p0,p1, valuecounts)
            e0 = nums[p0]
            e1 = nums[p1]
            if not e1 in valuecounts:
                valuecounts[e1] = 0
                if e1 > upper: upper = e1
                if e1 < lower: lower = e1
            valuecounts[e1] += 1

            if upper-lower <= 2:
                cont = True
                #print("Add new combinations from",p0,"tp",p1,"=",p1-p0+1)
                count += (p1-p0+1)
            
            prev0 = p0
            #if upper-lower > 2:
            #    print("upper, lower",upper,lower)
            while upper-lower > 2:
                #print("valuecounts",valuecounts)
                valuecounts[e0] -= 1
                if valuecounts[e0] == 0:
                    del valuecounts[e0]
                    if e0 == upper:
                        upper = max(valuecounts.keys())
                        #print("New upper",upper)
                    if e0 == lower:
                        lower = min(valuecounts.keys())
                        #print("New lower",lower)
                        
                p0 += 1
                e0 = nums[p0]

            if p0 != prev0:
                #print("final upper, lower",upper,lower)    
                combinations = 1+(p1 - p0)
                #combinations = ((p0-prev0)*(p0-prev0)-1)//2
                #print("Final p0-prev0",p0,prev0,"duration",p0-prev0,"combinations",combinations)
                count += combinations

            p1 += 1


        return count
