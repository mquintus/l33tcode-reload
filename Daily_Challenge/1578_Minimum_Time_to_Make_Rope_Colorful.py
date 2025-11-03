# 1578 - Minimum Time to Make Rope Colorful
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev = -1
        maximumRemove = []
        timeToRemove = 0
        for i, el in enumerate(colors):
            #print(el)
            if el != prev:
                maximumRemove = [neededTime[i]]
            else:
                if neededTime[i] > maximumRemove[-1]:
                    #print("Add",maximumRemove)
                    timeToRemove += maximumRemove.pop()
                    maximumRemove.append(neededTime[i])
                else:
                    timeToRemove += neededTime[i]
                    #print("Add",neededTime[i])
                
            prev = el

        return timeToRemove
