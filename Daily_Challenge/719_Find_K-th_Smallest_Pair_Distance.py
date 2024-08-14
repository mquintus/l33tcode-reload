# 719 - Find K-th Smallest Pair Distance
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        def howManyNeighbors(i, threshold):
            counter = 0
            a = i-1
            while a >= 0:
                t_a = abs(nums[i] - nums[a])
                if t_a > threshold: break
                a -= 1
                counter += 1
            return counter
        
        def howManyCompleteSlow(threshold):
            counter = 0
            for i in range(n):
                counter += howManyNeighbors(i, threshold)
            return counter

        def howManyComplete(threshold):
            counter = 0
            a = 0
            b = 1
            while b < n:
                t_a = nums[b] - nums[a]
                if t_a <= threshold:
                    counter += (b-a)
                    #print(threshold,b,a)
                    b += 1
                else:
                    if a < b - 1:
                        a += 1
                    else:
                        a += 1
                        b += 1               
            return counter


        # binary search
        start = 0
        end = nums[n-1] - nums[0]
        tries = 1000
        while start < end and tries > 0:
            tries -= 1
            mid = (start + end) // 2
            #print("Start, Mid, End", start,mid,end)
            howmany = howManyComplete(mid)

            if howmany == k:
                if mid == 0 or howManyComplete(mid-1) < k:
                    return mid
                else:
                    end = mid
            
            if howmany > k:
                end = mid
            elif howmany < k:
                start = mid + 1
                howmany_next = howManyComplete(mid+1)
                #print(mid, k,"th", howmany, howmany_next)
                #if howmany_next > k:
                #    return mid
            
            
        return end
