# 1545 - Find Kth Bit in Nth Binary String
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        S = [int(el) for el in "011100110110001"]

        # midpoints = [1,3,7,15] aka 2,4,8,16
        mk = 2
        while mk <= k:
            if mk == k: return "1"
            mk <<= 1

        k -= 1
        while len(S) <= k:
            inverted = [1 if el == 0 else 0 for el in S[::-1] ]
            S.append(1)
            S.extend(inverted)
            #print(S, len(S), k)
        return str(S[k])
        
