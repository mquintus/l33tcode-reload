# 2433 - Find The Original Array of Prefix Xor
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # We can replace in-place, not requiring any additional space
        previous = 0
        for i, n in enumerate(pref):
            x = previous ^ n
            pref[i] = x
            previous = n
            
        return pref
