# 1695 - Maximum Erasure Value
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        r = -1
        cont = set()
        points = 0
        mpoints = 0
        while r < len(nums) - 1:
            while  r < len(nums) - 1 and nums[r+1] not in cont:
                r += 1
                cont.add(nums[r])
                points += nums[r]
                mpoints = max(mpoints, points)
            #print(l,r,mpoints)
            points -= nums[l]
            cont.remove(nums[l])
            l += 1

        return mpoints
