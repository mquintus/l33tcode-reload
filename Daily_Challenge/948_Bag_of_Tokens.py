# 948 - Bag of Tokens
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        max_score = 0
        
        tokens.sort()

        while len(tokens):
            if score == 0 and tokens[0] > power:
                return score
            elif tokens[0] <= power:
                score += 1
                max_score = max(max_score, score)
                power -= tokens.pop(0)
            elif score > 0:
                score -= 1
                power += tokens.pop()

        return max_score
