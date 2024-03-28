# 2958 - Length of Longest Subarray With at Most K Frequency
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p1 = 0
        p2 = 0
        hashmap = {} # [0] * n 
        hashmap[nums[p1]] = 1
        bad = 0

        def add(k, i, hashmap, bad):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 0
            hashmap[nums[i]] += 1
            if hashmap[nums[i]] == k + 1:
                bad += 1
            return bad
        def remove(k, i, hashmap, bad):
            hashmap[nums[i]] -= 1
            if hashmap[nums[i]] == k:
                bad -= 1
            return bad

        maxlength = 0
        while p2 < n:   
            if bad > 0 and p1 == p2:
                bad = remove(k, p1, hashmap, bad)
                p1 += 1
                p2 += 1
                if p2 < n:
                    bad = add(k, p2, hashmap, bad)
            elif bad > 0 and p2 > p1:
                bad = remove(k, p1, hashmap, bad)
                p1 += 1
            elif bad == 0:
                p2 += 1
                if p2 < n:
                    bad = add(k, p2, hashmap, bad)

            if bad == 0:
                newlength = p2 - p1 + 1
                if p2 >= n:
                    newlength -= 1
                maxlength = max(maxlength, newlength)

        return maxlength
