# 1930 - Unique Length-3 Palindromic Subsequences
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        combinations = [[False] * 26 for _ in range(26)]
        counter = 0
        s = [ord(l) - ord('a') for l in s]

        right = Counter(s)
        left = {k:0 for k in right.keys()}
        #left[s[0]] -= 1
        right[s[0]] -= 1
        #right[s[1]] -= 1
        #print(left, right)

        maximumNumberOfCombinations = len(right.keys()) * len(right.keys())
        #print(maximumNumberOfCombinations)

        for i in range(1,len(s)):
            oldchar = s[i-1]
            midchar = s[i]

            right[midchar] -= 1
            left[oldchar] += 1

            #print(left, right)

            for letter in right.keys():
                if right[letter] > 0 and left[letter] > 0:
                    if not combinations[letter][midchar]:
                        counter += 1
                        combinations[letter][midchar] = True
            
            if count == maximumNumberOfCombinations: break

        return counter

