# 1930 - Unique Length-3 Palindromic Subsequences
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        '''
        A palindromic subsequence has a first letter, which repeats at the third position,
        and any letter in between.

        The first step is therefore to find the first and last occurence of each letter
        and make sure that there is space for another letter in between.

        Then, count the number of letters that are found in between, e.g.
        'aabcddddefa' will result in finding 'a' and 'a' and the answer is the
        number of distinct letters in between, i.e. 'abcdef' == 6

        '''
        # normalize the string
        s = [ord(c) - ord('a') for c in s]

        first_occurrence = [len(s)] * 26
        last_occurrence = [-1] * 26

        letters_found = set()

        found = 26
        for i, c in enumerate(s):
            last_occurrence[c] = i
            reverse_i = len(s) - i - 1
            first_occurrence[s[reverse_i]] = reverse_i
            letters_found.add(c)

        combinations = 0
        for letter in letters_found:
            f_index = first_occurrence[letter] 
            l_index = last_occurrence[letter]
            if f_index < l_index - 1:
                in_betweens = [0] * 26
                for c in s[f_index + 1:l_index]:
                    in_betweens[c] = 1
                combinations += sum(in_betweens)

        return combinations
