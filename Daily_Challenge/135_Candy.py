# 135 - Candy
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0
        result = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                minimal = result[i-1] + 1
                result[i] = minimal
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                minimal = result[i+1] + 1
                result[i] = max(minimal, result[i])
        
        #print(result)
        return sum(result)
        
        
