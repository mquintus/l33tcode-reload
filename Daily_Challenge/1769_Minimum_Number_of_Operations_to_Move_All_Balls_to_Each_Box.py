# 1769 - Minimum Number of Operations to Move All Balls to Each Box
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        prefixSum = 0
        prefixBox = [0]
        postfixBox = [0]
        n=len(boxes)
        totalSum = 0
        for i, one in enumerate(boxes):
            totalSum += int(one)
            prefixSum += (int(one)*i)
            prefixBox.append(prefixBox[-1] + int(one))
            postfixBox.append(postfixBox[-1] + int(boxes[-1-i]))
        #print(prefixBox)
        #print(postfixBox)
        solution = [
            prefixSum
        ]
        for i in range(0,len(boxes)-1):
            nextSolution = solution[i] 
            nextSolution -= postfixBox[n-i-1] 
            nextSolution += prefixBox[i+1]
            solution.append(nextSolution)
            
            
        return solution


        
