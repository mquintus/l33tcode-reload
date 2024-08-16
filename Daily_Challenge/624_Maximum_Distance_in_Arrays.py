class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minnum = arrays[0][0]
        maxnum = arrays[0][-1]
        result = 0
        for arr in arrays[1:]:
            distance1 = maxnum - arr[0]
            distance2 = arr[-1] - minnum
            distance = max(distance1, distance2)
            result = max(result, distance)
            #print(distance1, distance2)
            #print("distance, result",distance, result)
            #print("Result:",maxnum,minnum, "distance:", distance)
            minnum = min(minnum, arr[0])
            maxnum = max(maxnum, arr[-1])
            #print("New minnum", minnum)
            #print("New maxnum", maxnum)

        return result
