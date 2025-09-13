# 3541 - Find Most Frequent Vowel and Consonant
class Solution:
    def maxFreqSum(self, s: str) -> int:
        mv = max([s.count('a'), s.count('e'), s.count('i'), s.count('o'), s.count('u')])
        c = Counter(s)
        t = sorted([(f, el) for el, f in c.items() if el not in 'aeiou'])
        if len(t) == 0: return mv
        #print(mv, t)
        return mv + t[-1][0]
