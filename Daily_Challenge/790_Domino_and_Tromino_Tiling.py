# 790 - Domino and Tromino Tiling
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9+7
        seq = [1,1,2,5,11,24,53,117]
        for i in range(len(seq), n+1):
            seq.append((seq[-1]*2 + seq[-3])%MOD)
        return seq[n]
