# 2900 - Longest Unequal Adjacent Groups Subsequence I
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = [words[0]]
        bit = groups[0]
        for i in range(len(groups)):
            if groups[i] != bit:
                bit = groups[i]
                result.append(words[i])
        return result
