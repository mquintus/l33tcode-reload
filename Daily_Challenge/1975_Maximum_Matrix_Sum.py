# 1975 - Maximum Matrix Sum
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        allElements = []
        for row in matrix:
            allElements.extend(row)
        
        # How many negative elements are there?
        # If it's even, we can take the abs(), or there is a zero
        # If it's odd, one on them stays negative: The one with the smallest abs
        
        numberOfNegatives = 0
        smallestAbsNegative = float('inf')
        hasZero = False
        for el in allElements:
            if el == 0:
                hasZero = True
            elif el < 0:
                numberOfNegatives += 1

            if abs(el) < smallestAbsNegative:
                smallestAbsNegative = abs(el)
        

        if hasZero or numberOfNegatives % 2 == 0:
            return sum([abs(el) for el in allElements])
        else:
            return sum([abs(el) for el in allElements]) - 2*smallestAbsNegative
        
