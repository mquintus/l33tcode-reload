# 2138 - Divide a String Into Groups of Size k
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        for i in range(((k-1)+(len(s)))//k):
            result.append(s[i*k:(i+1)*k])
        if len(result[-1]) < k:
            result[-1] += fill*(k-len(result[-1]))
        return result
