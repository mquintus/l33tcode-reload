# 58 - Length of Last Word
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) < 2:
            return True

        translations = {}
        used = set()
        for i, el in enumerate(s):
            el2 = t[i]
            if el not in translations:
                translations[el] = el2
                if el2 in used:
                    return False
                used.add(el2)
            else:
                if translations[el] != el2:
                    return False

        return True
        
        
