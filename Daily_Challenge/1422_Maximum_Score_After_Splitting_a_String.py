# 1422 - Maximum Score After Splitting a String
class Solution:
    def maxScore(self, s: str) -> int:
        maxscore = 0
        score = sum([int(el) for el in s])
        for el in s[:-1]:
            if el == "1":
                score -= 1
            else:
                score += 1
            maxscore = max(score, maxscore)
        return maxscore
