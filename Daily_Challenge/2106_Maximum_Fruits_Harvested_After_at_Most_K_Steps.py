# 2106 - Maximum Fruits Harvested After at Most K Steps
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        bestValue = 0
        positions, value = [a for [a,b] in fruits], [b for [a,b] in fruits]
        

        #print("Going mostly left and a little bit right")
        rightmostPositionPrev = -1
        currentValue = 0
        # a little bit to the right and the rest still left
        for leftmostFruit in range(0, bisect.bisect_left(positions, startPos)):
            #print("I try to get fruit",leftmostFruit)
            leftmostPosition = positions[leftmostFruit]
            stepsUsedToLeft = startPos - leftmostPosition
            if stepsUsedToLeft > k: 
                #print("But it is too far")
                rightmostPositionPrev = leftmostFruit
                continue
            stepsAvailableToRight = (k - stepsUsedToLeft) // 2
            #print("steps used",stepsUsedToLeft,"leaving me with",stepsAvailableToRight,"steps to the right")
            rightmostPosition = startPos + stepsAvailableToRight
            maxRightIndex = bisect.bisect_left(positions, rightmostPosition+1) - 1 
            #print("and I can also get fruit", maxRightIndex)
            currentValue += sum(value[rightmostPositionPrev+1:maxRightIndex+1])
            #print("adding values",maxRightIndex,"to",rightmostPositionPrev+1,":", value[rightmostPositionPrev+1:maxRightIndex+1])
            bestValue = max(bestValue, currentValue)
            #print("Price:",currentValue)
            rightmostPositionPrev = maxRightIndex
            currentValue -= value[leftmostFruit]

        #print()
        #print("Going mostly right and a little bit left")
        leftmostPositionPrevIndex = positions[-1]+1
        currentValue = 0
        #print("Reset value to", currentValue)
        # a little bit to the right and the rest still left
        for rightmostFruit in range(len(fruits)-1,bisect.bisect_left(positions, startPos)-1,-1):
            #print("I try to get fruit",rightmostFruit)
            rightmostPosition = positions[rightmostFruit]
            stepsUsedToRight = rightmostPosition - startPos
            if stepsUsedToRight > k: 
                #print("But it is too far",rightmostPosition,">",startPos,"+",k)
                leftmostPositionPrevIndex = rightmostFruit
                continue
            stepsAvailableToLeft = (k - stepsUsedToRight) // 2
            #print("leaving me with",stepsAvailableToLeft,"steps to the left")
            leftmostPosition = startPos - stepsAvailableToLeft
            maxLeftIndex = bisect.bisect_left(positions, leftmostPosition) 
            #print("and I can also get fruit", maxLeftIndex)
            currentValue += sum(value[maxLeftIndex:leftmostPositionPrevIndex])
            #print("adding values",maxLeftIndex,"to",leftmostPositionPrevIndex,":", value[maxLeftIndex:leftmostPositionPrevIndex])
            bestValue = max(bestValue, currentValue)
            leftmostPositionPrevIndex = maxLeftIndex
            #print("Price:",currentValue)
            currentValue -= value[rightmostFruit]
            #print("Without the rightmost fruit", currentValue)

        
        return bestValue
