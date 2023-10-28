# 1220 - Count Vowels Permutation
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9+7
        rules = {
            'a': ['e'],
            'e': ['a', 'i'],
            'i': ['a', 'e', 'o', 'u'],
            'o': ['i', 'u'],
            'u': ['a']
        }

        last_letter = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1}

        for i in range(n-1):
            added_letters = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
            for l, c in last_letter.items():
                for follow in rules[l]:
                    added_letters[follow] += c
                    added_letters[follow] %= MOD
            last_letter = added_letters
        
        return sum(last_letter.values()) % MOD
