# 3335 - Total Characters in String After Transformations I
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        counts = [0] * 26
        for el in s:
            o = ord(el) - ord('a')
            counts[o] += 1
        

        for _ in range(t):
            a = counts[25]
            b = counts[25]
            for i in range(25, 0, -1):
                counts[i] = counts[i - 1]
            counts[0] = a % MOD
            counts[1] += b
        
        return sum(counts) % MOD
