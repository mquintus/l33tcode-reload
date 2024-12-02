# 1455 - Check If a Word Occurs As a Prefix of Any Word in a Sentence
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        n = len(searchWord)
        for i, word in enumerate(sentence.split()):
            if word[:n] == searchWord: return i + 1
        return -1
