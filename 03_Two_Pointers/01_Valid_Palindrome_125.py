class Solution:
    relevent_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5','6','7','8','9']

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        k = len(s) - 1
        while i < len(s):
            if s[i] not in self.relevent_chars:
                i += 1
                continue
            if s[k] not in self.relevent_chars:
                k -= 1
                continue
            if s[i] == s[k]:
                i += 1
                k -= 1
            else:
                return False
        return True
