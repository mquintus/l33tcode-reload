# 862 - Shortest Subarray with Sum at Least K
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        result = 10**9

        cumulsum = [0]
        for i, el in enumerate(nums):
            cumulsum.append(cumulsum[-1] + el)
            if el >= k: return 1
            if cumulsum[-1] >= k: 
                result = min(result, i+1)
                #print("cumulsum",cumulsum)
        #print("result A",result)

        p0 = 0
        p1 = -1
        dp=[0]*len(nums)
        for i, cumu in enumerate(cumulsum):
            while p0 <= p1 and cumu - cumulsum[dp[p0]] >= k:
                #print("Found ",i-dp[p0], "between", p0, p1)
                result = min(result, i-dp[p0])
                #print("result",result)
                p0 += 1
            while p0 <= p1 and cumu <= cumulsum[dp[p1]]:
                p1 -= 1
            p1 += 1 
            if p1 >= len(nums): break
            dp[p1] = i

        if result == 10**9: return -1
        return result
            
