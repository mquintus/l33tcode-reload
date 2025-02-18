# 2375 - Construct Smallest Number From DI String
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = ''
        p = 0
        c = 1
        while p < len(pattern):
            for i, el in enumerate(pattern[p:]):
                if el == 'I':
                    break
            else:
                i += 1
            result += ''.join([str(ch) for ch in range(c, c+i+1)[::-1]])
            p += (i+1)
            c = c + (i+1)
        if p == len(pattern):
            result += str(c)
        return result
