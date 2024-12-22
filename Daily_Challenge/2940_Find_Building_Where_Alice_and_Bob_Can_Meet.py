# 2940 - Find Building Where Alice and Bob Can Meet
class Solution:
    def leftmostBuildingQueries(self, heights, queries):
        qn = len(queries)
        answer = [-1 for _ in range(qn)]
        newqueries = []
        for i, (a,b) in enumerate(queries):
            if a==b: 
                answer[i] = a
                continue
            if a > b:
                a,b=b,a
            if heights[b] > heights[a]: 
                answer[i] = b
                continue
            if b == len(heights)-1: 
                answer[i] = -1
                continue
            newqueries.append((b-1, heights[a], i))
        newqueries.sort()
        newqueries = newqueries[::-1]

        def binary_search(monostack, minheight):
            start = 0
            end = len(monostack)
            while end > start:
                mid = (start+end)//2
                if monostack[mid][0] <= minheight: #invalid
                    if mid == 0:
                        return -1
                    if monostack[mid-1][0] > minheight: # if the previous is valid, take it.
                        return monostack[mid-1][1]
                    end = mid
                else: # valid
                    if mid == len(monostack)-1: # if this is the most recent, take it.
                        return monostack[mid][1]
                    if monostack[mid+1][0] <= minheight: # If the more recent one is invalid, don't look further.
                        return monostack[mid][1]
                    start = mid+1
            return -1

        monostack = []
        hn = len(heights) - 1
        i = hn
        for right, minheight, qidx in newqueries:
            while i > right:
                h = heights[i]
                while monostack and h > monostack[-1][0]:
                    monostack.pop()
                monostack.append((h, i))
                i -= 1
            # the biggest (oldest) element in the monostack is monostack[0]
            # is the biggest element is too small, don't do binary search
            if monostack[0][0] <= minheight: continue 
            answer[qidx] = binary_search(monostack, minheight)
        return answer
