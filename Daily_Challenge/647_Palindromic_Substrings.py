# 647 - Palindromic Substrings
class Solution:
    def countSubstrings(self, s: str) -> int:
        self.number_of_p = 0
        n = len(s)

        def check_for_palindrome(midpoint):
            if midpoint == int(midpoint):
                self.number_of_p += 1
                left = midpoint - 1
                right = midpoint + 1
            else:
                left = int(midpoint - .5)
                right = int(midpoint + .5)

            while left >= 0 and right < n and s[left] == s[right]:
                self.number_of_p += 1
                left -= 1
                right += 1
            
        for midpoint in range(0, len(s)):
            check_for_palindrome(midpoint)
            check_for_palindrome(midpoint + .5)

        return self.number_of_p
