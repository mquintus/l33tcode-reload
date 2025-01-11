# 1400 - Construct K Palindrome Strings
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False
        if len(s) == k: return True

        count = [0 for _ in range(26)]
        for idx in range(26):
            count[idx] = s.count(chr(idx + ord('a'))) % 2

        number_of_odd = 0
        for idx in range(26):
            if count[idx]: 
                number_of_odd += 1

        return number_of_odd <= k
