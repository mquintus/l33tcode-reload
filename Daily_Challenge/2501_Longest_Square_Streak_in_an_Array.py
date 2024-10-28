# 2501 - Longest Square Streak in an Array
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        largestRoot = int(100000**.5)
        
        knownSquares = {}
        visited = set()
        longestStreak = -1
        for el in nums:
#            if el > largestRoot: continue
            if el in visited: continue
            visited.add(el)
            
            minEl = el
            maxEl = el
            streak = 1

            square = el**2
            maxEl = square
            if square in knownSquares:
                maxEl = knownSquares[square][1]
                streak += knownSquares[square][2]
            
            if el in knownSquares:
                minEl = knownSquares[el][0]
                streak += knownSquares[el][2]

            newTuple = (minEl, maxEl, streak)
            knownSquares[el] = newTuple
            knownSquares[minEl] = newTuple
            knownSquares[maxEl] = newTuple
            #print(el, newTuple)
            if streak > 1:
                longestStreak = max(streak, longestStreak)

        return longestStreak
