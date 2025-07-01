# 3330 - Find the Original Typed String I
class Solution:
    def possibleStringCount(self, word: str) -> int:
        answer = 1
        prev = word[0]
        for el in word[1:]:
            if el == prev:
                answer += 1
            prev = el
        return answer
