# 2131 - Longest Palindrome by Concatenating Two Letter Words
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        length = 0
        middle = 0
        wordset = Counter(words)
        for word in words:
            a = word[0]
            b = word[1]
            if f"{b}{a}" in wordset and wordset[f"{b}{a}"] > 0 and wordset[f"{a}{b}"] > 0:
                if a == b:
                    if wordset[f"{a}{b}"] == 1:
                        middle = 2
                        continue
                length += 4
                wordset[f"{b}{a}"] -= 1
                wordset[f"{a}{b}"] -= 1
        return length + middle
