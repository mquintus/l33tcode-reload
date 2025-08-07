# 3363 - Find the Maximum Number of Fruits Collected
class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        child1 = 0
        for i in range(n):
            child1 += fruits[i][i]
            fruits[i][i] = 0
        
        r = n-1
        c = 0
        prev_min_r = n-1        
        prev_prev_min_r = n-1
        for c in range(1, n):
            prev_min_r = max(c+1, prev_min_r-1)
            for r in range(prev_min_r, n):
                best = 0
                for prev_r in range(max(r-1,prev_prev_min_r), min(n, r+2)):
                    best = max(best, fruits[prev_r][c-1])
                fruits[r][c] += best
            prev_prev_min_r = prev_min_r
        child2 = fruits[n-1][n-2]

        r = n-1
        c = 0
        prev_min_r = n-1        
        prev_prev_min_r = n-1
        for c in range(1, n):
            prev_min_r = max(c+1, prev_min_r-1)
            for r in range(prev_min_r, n):
                best = 0
                for prev_r in range(max(r-1,prev_prev_min_r), min(n, r+2)):
                    best = max(best, fruits[c-1][prev_r])
                fruits[c][r] += best
            prev_prev_min_r = prev_min_r
        child3 = fruits[n-2][n-1]
        

        return child1 + child2 + child3
            
