# 1935 - Maximum Number of Words You Can Type
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        counter = 0
        for word in text.split(' '):
            for bl in brokenLetters:
                if bl in word:
                    break
            else:
                counter += 1
        return counter
