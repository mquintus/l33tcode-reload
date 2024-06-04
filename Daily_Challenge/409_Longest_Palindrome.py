# 409 - Longest Palindrome
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        has_indiv = False
        result = 0
        for value in counts.values():
            result += 2 * (value // 2)
            if not has_indiv and value % 2 == 1:
                result += 1
                has_indiv = True
        return result
