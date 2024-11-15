# 1574 - Shortest Subarray to be Removed to Make Array Sorted
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        
        p0 = 0
        p1 = n-1
        while p0 < n-1 and arr[p0+1] >= arr[p0]:
            p0+=1
        if p0 == n-1:
            return 0
        while p1 > 1 and arr[p1-1] <= arr[p1]:
            p1-=1

        # Sliding window of fixed size:
        def slide(windowsize):
            for s0 in range(p1-windowsize-1, p0+1):
                s1 = s0+windowsize+1
                #print("Window", s0, s1, windowsize)
                #if s1 <= n-1 and s0 >= 0:
                    #print("Values", arr[s0], arr[s1])
                if s1 >= n or s0 <= -1 or arr[s1] >= arr[s0]:
                    #print("Remove between",s0, s1)
                    return True
            return False

        minwindowsize = p1 - p0 - 1
        maxwindowsize = n
        result = False
        #print(p0, p1)
        while maxwindowsize > minwindowsize:
            mid = (maxwindowsize + minwindowsize) // 2
            #print("Window sizes considered", minwindowsize, mid, maxwindowsize)
            if slide(mid):
                #print("Solution found for", mid)
                if not slide(mid-1):
                    #print("but",mid-1,"not possible")
                    break
                else:
                    maxwindowsize = mid
            else:
                minwindowsize = mid + 1
        return mid
