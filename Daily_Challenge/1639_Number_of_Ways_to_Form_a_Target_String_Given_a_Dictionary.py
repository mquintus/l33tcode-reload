# 1639 - Number of Ways to Form a Target String Given a Dictionary
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(target)
        m = len(words)
        m1 = len(words[0])
        MOD = 10**9+7
       
         
        freq = [[0]*300 for _ in range(m1+1)]
        for word in words:
            for a in range(m1):
                freq[a][ord(word[a])] += 1

        @cache
        def rec(t, idx):
            if t == n:
                return 1
            if idx == m1:
                return 0
            skip = rec(t, idx+1)
            targetletter = target[t]
            take = (rec(t+1, idx+1) * freq[idx][ord(targetletter)])
            ways = take+skip
            return ways % MOD

        return rec(0, 0)

            
