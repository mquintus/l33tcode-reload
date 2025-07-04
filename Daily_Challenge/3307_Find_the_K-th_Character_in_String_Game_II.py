# 3307 - Find the K-th Character in String Game II
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        k -= 1
        #print("Starting with k", k)
        if k == 0: return "a"

        f = 1
        p = 0
        while f*2 <= k:
            p += 1
            f *= 2
        
        #print(k, "means exponent",p, "which refers to a length of", f )

        actions = []
        diff = 0
        while k > 0:
            if f > k:
                f //= 2
                p -= 1
                continue
            #print("k - f", k, "-", f, "=",k-f)
            
            k -= f
            o = operations[p]
            
            if o == 1:
                diff += 1
            #print("Looking at letter", k, "operation", p, "is", o, "plus a diff of", diff)
            
            if k == 0: break
            
            
        return chr(ord('a')+(diff % 26))
        
