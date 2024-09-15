# 1371 - Find the Longest Substring Containing Vowels in Even Counts
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)
        vowels = {
            'a': 1,
            'e': 2,
            'i': 4,
            'o': 8,
            'u': 16,
        }
        bits = [0]*(n+1)
        for vowel,bit in vowels.items():
            val = 0
            for i,l in enumerate(s):
                if l == vowel:
                    val ^= bit
                bits[i+1] ^= val
        #print(bits)

        values = Counter(bits)
        #print(values)


        best_result = 0
        for value in values.keys():
            first = -1
            last = -1
            for i,l in enumerate(bits):
                if l == value:
                    last = i
                    if first == -1:
                        first = i
            dist = last-first
            #print(value,first,last,dist)
            #print(s[first:last])
            best_result = max(best_result, dist)

        return best_result
