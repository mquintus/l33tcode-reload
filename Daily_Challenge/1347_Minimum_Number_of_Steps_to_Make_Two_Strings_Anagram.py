# 1347 - Minimum Number of Steps to Make Two Strings Anagram
class Solution:
    def minSteps(self, s: str, t: str) -> int:

        p = Counter(s)
        q = Counter(t)

        equals = 0
        for key, value in p.items():
            if key in q.keys():
                equals += min(value, q[key]) 

        unequals = len(s) - equals

        return unequals
