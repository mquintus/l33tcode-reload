# 1846 - Maximum Element After Decreasing and Rearranging
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        mymax = 1 
        prev = 1
        arr[0] = 1
        for a in arr:
            if a > prev+1:
                a = prev+1
            prev = a
            mymax = max(mymax, a)
        return mymax
