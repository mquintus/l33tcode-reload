# 2483 - Minimum Penalty for a Shop
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pY = [0]
        pN = [0]
        n = len(customers)
        for i in range(n):
            isY = 0 if customers[i] == 'Y' else 1
            pY.append(pY[-1] + isY)
            j = n - 1 - i
            isN = 0 if customers[j] == 'N' else 1
            pN.append(pN[-1] + isN)
        pN.reverse()
        pN.append(0)
        pY.append(pY[-1])
        minP = float('inf')
        for i in range(n+1):
            currP = pY[i]+pN[i]
            minP = min(minP, currP)
            #print(pY[i], pN[i], currP)
            
        for i in range(n+1):
            currP = pY[i]+pN[i]
            if currP == minP:
                return i        
