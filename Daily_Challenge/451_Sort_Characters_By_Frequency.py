# 451 - Sort Characters By Frequency
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        return "".join([k*v for k, v in sorted(list(c.items()), reverse=True, key=lambda x: x[1])])
