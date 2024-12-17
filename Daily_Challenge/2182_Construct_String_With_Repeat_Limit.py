# 2182 - Construct String With Repeat Limit
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        c = Counter(s)
        lexi = sorted([[el, count] for el, count in c.items()])[::-1]
        prev = ''
        result = []
        while True:
            first = True
            for i, (el, count) in enumerate(lexi):
                if count == 0: continue
                if el == prev: 
                    first = False
                    continue
                if not first: count = 1
                newcount = min(count, repeatLimit)
                result.append(el*newcount)
                lexi[i][1] -= newcount
                prev = el
                break
            else:
                break
        return "".join(result)
