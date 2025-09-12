# 3227 - Vowels Game in a String
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        c = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
        if c == 0:
            return False
        return True
