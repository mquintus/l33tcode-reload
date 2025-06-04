# 3403 - Find the Lexicographically Largest String From the Box I
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        if numFriends == 1: return word
        longest_length = n - numFriends + 1
        highest_letter = max(set(list(word)))
        start = word.index(highest_letter)
        final = word[start]
        for i in range(start,n):
            final = max(final,word[i:i+longest_length])
        return final
