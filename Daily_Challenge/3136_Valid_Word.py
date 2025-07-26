# 3136 - Valid Word
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False
        vowels = set("aeiouAEIOU")
        upper = 'bcdfghjklmnpqrstvwxyz'.upper()
        consonant = set('bcdfghjklmnpqrstvwxyz' + upper)
        numbers = set("0123456789")
        hasV = False
        hasC = False
        for letter in word:
            if letter not in vowels and letter not in consonant  and letter not in numbers:
                return False
            if letter in vowels:
                hasV = True
            if letter in consonant:
                hasC = True
        if not hasV or not hasC:
            return False
        return True
