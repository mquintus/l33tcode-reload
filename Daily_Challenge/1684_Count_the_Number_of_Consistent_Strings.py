# 1684 - Count the Number of Consistent Strings
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow = [False] * 200
        for c in allowed:
            allow[ord(c)] = True
        del c
        counter = 0
        for word in words:
            for char in word:
                if not allow[ord(char)]:
                    break
            else:
                counter += 1
        return counter
