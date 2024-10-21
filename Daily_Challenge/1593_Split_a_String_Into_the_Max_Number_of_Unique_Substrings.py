# 1593 - Split a String Into the Max Number of Unique Substrings
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        splits = set()
        validSolutions = 0
        def split(i):
            if i == len(s): 
                nonlocal validSolutions
                validSolutions = max(validSolutions, len(splits))
                return True
            l = 1
            found_solution = False
            while i+l <= len(s):
                while s[i:i+l] in splits and i+l <= len(s):
                    l += 1    
                if i+l > len(s):
                    return False
                splits.add(s[i:i+l])
                found_solution = split(i+l)
                splits.remove(s[i:i+l])
                l += 1
            return False
        split(0)
        return validSolutions
