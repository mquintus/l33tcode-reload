# 2140 - Solving Questions With Brainpower
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        df = [-1] * n
        
        df[n-1] = questions[n-1][0]
        for i in range(n-2,-1,-1):
            # Return the number of points you can get
            take = questions[i][0]
            seq = i + questions[i][1] + 1
            if seq < n:
                take += df[seq]
            skip = df[i + 1]
            df[i] = max(take, skip)

        return df[0]
