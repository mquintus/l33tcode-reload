# 2785 - Sort Vowels in a String
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {}
        vowel_list = 'AEIOUaeiou'

        for v in vowel_list:
            vowels[v] = 0 

        positions = []
        for i, c in enumerate(s):
            if c in vowel_list:
                vowels[c] += 1
                positions.append(i)
        
        new_word = list(s)
        v_index = -1
        for i in positions:
            while v_index == -1 or vowels[v] == 0:
                v_index += 1
                v = vowel_list[v_index]
            new_word[i] = v
            vowels[v] -= 1
        
        return "".join(new_word)
