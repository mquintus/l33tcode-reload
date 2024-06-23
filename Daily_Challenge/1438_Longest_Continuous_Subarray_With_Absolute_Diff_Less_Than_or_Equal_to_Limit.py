# 1438 - Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        elsmap = {}
        elsmin = []
        elsmax = []
        p0 = 0
        p1 = 0
        elsmap[nums[p0]] = 1
        elsmin = [nums[p0]]
        elsmax = [-nums[p0]]
        peaklength = 0

        while p0 < n:
            diff = -elsmax[0] - elsmin[0]
            #print(diff, '=', elsmin[0], -elsmax[0])
            if diff <= limit:
                peaklength = max(peaklength, p1-p0+1)
                p1 += 1
                if p1 >= n:
                    break
                if nums[p1] not in elsmap:
                    elsmap[nums[p1]] = 0
                elsmap[nums[p1]] += 1
                heapq.heappush(elsmin, nums[p1])
                heapq.heappush(elsmax, -nums[p1])
            if p1 >= n:
                break
            while diff > limit:
                remove_el = nums[p0]
                elsmap[remove_el] -= 1
                p0 += 1
                if p0 >= n:
                    break
                minel = elsmin[0]
                while elsmap[minel] == 0:
                    heapq.heappop(elsmin)
                    minel = elsmin[0]
                maxel = -elsmax[0]
                #print("maxel",maxel,elsmap,elsmax)
                while elsmap[maxel] == 0:
                    heapq.heappop(elsmax)
                    maxel = -elsmax[0]
                diff = maxel - minel

                minel = elsmin[0]
                maxel = -elsmax[0]
            if p0 >= n:
                break


                diff = -elsmax[-1] - elsmin[0]
                

        return peaklength
