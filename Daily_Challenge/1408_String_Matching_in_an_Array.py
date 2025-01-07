# 1408 - String Matching in an Array
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        answer = []
        n = len(words)
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if len(words[i]) >= len(words[j]): continue
                li = len(words[i])
                if words[i] in words[j]:
                    answer.append(words[i])
                    break
        return answer
