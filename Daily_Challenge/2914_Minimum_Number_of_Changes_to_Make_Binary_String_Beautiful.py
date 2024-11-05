# 2914 - Minimum Number of Changes to Make Binary String Beautiful
def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)

class Solution:
    def minChanges(self, s: str) -> int:
        return sum([1 for el,le in pairwise(s) if el!=le])
