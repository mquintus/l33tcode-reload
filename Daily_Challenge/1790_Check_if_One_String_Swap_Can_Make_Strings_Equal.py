# 1790 - Check if One String Swap Can Make Strings Equal
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if Counter(s1) != Counter(s2): return False
        wrong = -1
        wrong_count = 0
        for i in range(len(s1)):
            if s1[i] == s2[i]: continue
            if wrong == -1:
                wrong = i
                wrong_count = 1
                continue
            else:
                if wrong_count > 1: return False
                wrong_count += 1
                if s1[wrong] == s2[i] and s2[wrong] == s1[i]:
                    continue
                return False
        return True
