# 1298 - Maximum Candies You Can Get from Boxes
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        alreadyOpened = [False]  * n 
        hasKey = status
        hasBox = set(initialBoxes)
        boxArr = []
        for box in hasBox:
            if hasKey[box]:
                boxArr.append(box)
        
        candyCount = 0
        while len(boxArr):
            currBox = boxArr.pop()
            #print("Open",currBox)
            if alreadyOpened[currBox]: continue
            alreadyOpened[currBox] = True

            candyCount += candies[currBox]

            for newKey in keys[currBox]:
                #print("Find key",newKey)
                if newKey in hasBox:
                    #print("Matching box!")
                    boxArr.append(newKey)
                    hasKey[newKey] = False
                    hasBox.remove(newKey)
                    continue
                else:
                    hasKey[newKey] = True

            for newBox in containedBoxes[currBox]:
                #print("Find box",newBox)
                if hasKey[newBox]:
                    #print("Matching key!")
                    boxArr.append(newBox)
                    hasKey[newBox] = False
                    continue
                hasBox.add(newBox)
        return candyCount


