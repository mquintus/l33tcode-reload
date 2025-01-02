# 2559 - Count Vowel Strings in Ranges
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefixSum = [0]
        vowels = 'aeiou'
        c = 0
        for w in words:
            if w[0] in vowels and w[-1] in vowels:
                c+=1
            prefixSum.append(c)
        prefixSum.append(c)
        answers = []
        for f,t in queries:
            answers.append(prefixSum[t+1] - prefixSum[f])
        return answers
