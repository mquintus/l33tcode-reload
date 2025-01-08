# 3042 - Count Prefix and Suffix Pairs I
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(a,b):
            l = len(a)
            return a == b[:l] and a == b[-l:]

        counter = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                counter += isPrefixAndSuffix(words[i], words[j])
        
        return counter
