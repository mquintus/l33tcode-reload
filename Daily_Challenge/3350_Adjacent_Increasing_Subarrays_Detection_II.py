# 3350 - Adjacent Increasing Subarrays Detection II
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        lengths = [1]
        prev = nums[0]
        for el in nums[1:]:
            if el > prev:
                lengths.append(lengths[-1] + 1)
            else:
                lengths.append(1)
            prev = el
        

        def binary_search(start, end, i):
            localmaxk = float('-inf')
            while start < end:
                mid = (start + end) // 2
                #print("binary search", start, mid, end)
                #print("Here, at index", mid, "we test for equality of it's value",lengths[mid]," with index ",i)
                if mid == i + lengths[mid]:
                    localmaxk = max(localmaxk, lengths[mid])
                    #print("Binary search found", mid, "with", lengths[mid])
                    start = mid + 1
                else:
                    end = mid
            return localmaxk

        #print(lengths)

        maxk = 0
        for i, le in enumerate(lengths):
            #print("What if sequence ended at including",i )
            maxk = max(maxk, le // 2)

            j = i + le
            if j >= n:
                if lengths[n-1] == n-1-i:
                    l2 = min(lengths[n-1], n-1-i)
                    #print("l2", l2)
                    maxk = max(maxk, l2)
                    break
                j = n - 1
                le2 = min(n - 1 - i, lengths[j])
            else:
                le2 = lengths[j]

            if le <= le2:
                #print("le",le,"le2",le2)
                maxk = max(maxk, le)
            elif le > maxk:
                localmaxk = binary_search(i+maxk, j+1, i)
                maxk = max(maxk, localmaxk)
                

        return maxk
            
