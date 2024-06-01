# 3110 - Score of a String
class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        a = ord(s[0])
        for b in s[1:]:
            score += abs(a-ord(b))
            a = ord(b)
        return score
