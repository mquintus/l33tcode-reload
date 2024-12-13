# 2593 - Find Score of an Array After Marking All Elements
class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        indexlist = []
        heap = []
        for i, el in enumerate(nums):
            element = [el, i, False]
            indexlist.append(element)
            heapq.heappush(heap, element)

        score = 0
        while heap:
            element = heapq.heappop(heap)
            el, i, marked = element
            if marked: 
                #print("Index",i,"Value",el,"Already marked") 
                continue
            score += el
            #print("Index",i,"Value",el,"Score",score)
            indexlist[i][2] = True
            if i > 0:
                indexlist[i-1][2] = True
            if i < n - 1:
                indexlist[i+1][2] = True

        return score
