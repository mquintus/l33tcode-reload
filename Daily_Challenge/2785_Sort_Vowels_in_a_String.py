# 2785 - Sort Vowels in a String
class Solution:
    def sortVowels(self, s: str) -> str:
        vowOrder = 'AEIOUaeiou'
        vowSet = set('AEIOUaeiou')
        vowels = {char: 0 for char in vowSet}
        
        for char in s:
            if char in vowSet:
                vowels[char] += 1

        t = list(s)
        for i, el in enumerate(t):
            if el in vowSet:
                for v in vowOrder:
                    c = vowels[v]
                    if c > 0:
                        t[i] = v
                        vowels[v] -= 1
                        break
        
        return ''.join(t)


