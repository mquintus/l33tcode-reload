# 1422 - Maximum Score After Splitting a String
class Solution:
    def maxScore(self, s: str) -> int:
        scoreleft = [0]
        scoreright = [0]
        n = len(s)
        for i in range(n):
            l = 0
            if s[i] == '0':
                l = 1
            scoreleft.append(scoreleft[-1] + l)

            r = 0            
            if s[n-i-1] == '1':
                r = 1
            scoreright.append(scoreright[-1] + r)

        #print(scoreleft, scoreright)
        maxscore = 0
        for i in range(1,n):
            score = scoreleft[i] + scoreright[n-i]
            maxscore = max(maxscore,score)

        return maxscore
