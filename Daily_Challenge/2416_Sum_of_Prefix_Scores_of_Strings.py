# 2416 - Sum of Prefix Scores of Strings
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        hashings = {}
        for word in words:
            for end in range(1,len(word)+1):
                token = word[:end]
                if token not in hashings:
                    hashings[token] = 0
                hashings[token] += 1
        #print(hashings)
        result = []
        for word in words:
            result.append(0)
            for end in range(1,len(word)+1):
                token = word[:end]
                result[-1] += hashings[token]
        return result
        
