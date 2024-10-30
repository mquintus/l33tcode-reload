# 1671 - Minimum Number of Removals to Make Mountain Array
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        inc = [1] * n
        dec = [1] * n
        
        for i in range(n-1):
            ni = n - i - 1
            for j in range(i+1,n):
                if nums[j] > nums[i]:
                    inc[j] = max(inc[j], inc[i] + 1)
                nj = n - j - 1
                if nums[ni] < nums[nj]:
                    #print(nj,dec[nj],ni,dec[ni])
                    dec[nj] = max(dec[nj], dec[ni] + 1)
        #print(inc, dec)
        
        longestMointain = 0
        for i in range(1, n - 1):
            if inc[i] > 1 and dec[i] > 1:
                longestMointain = max(longestMointain, inc[i] + dec[i] - 1)

        return n - longestMointain
        
