# 2707 - Extra Characters in a String
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        leftovers = [float('inf') for i in range(n)]
        def mymatch(word_index):
            if word_index == n:
                return 0
            if leftovers[word_index] != float('inf'):
                return leftovers[word_index]
            for word in dictionary:
                #print(word_index, word, s[word_index:word_index+len(word)])
                if word_index+len(word) <= n and s[word_index:word_index+len(word)] == word:
                    value = mymatch(word_index+len(word))
                    leftovers[word_index] = min(value, leftovers[word_index])
            if word_index < n:
                value = 1 + mymatch(word_index+1)
                leftovers[word_index] = min(value, leftovers[word_index])
            return leftovers[word_index]
        mymatch(0)
        return leftovers[0]
