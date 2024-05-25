# 140 - Word Break II
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        @cache
        def trackback(i):
            if i == n:
                return []
            solutions = []
            for word in wordDict:
                lenword = len(word)
                if s[i:i+lenword] == word:
                    followup = trackback(i+lenword)
                    if followup != False:
                        if len(followup) == 0:
                            solutions.append([word])
                        else:
                            for f in followup:
                                solutions.append([word, *f])
            if len(solutions) == 0:
                return False
            return solutions
        answer = trackback(0)
        if answer == False:
            return []
        return [" ".join(a) for a in answer]
