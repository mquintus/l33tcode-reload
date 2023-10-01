# 557 - Reverse Words in a String III
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        words = map(lambda x: x[::-1], words)
        return " ".join(words)
