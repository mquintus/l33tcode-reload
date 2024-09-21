# 386 - Lexicographical Numbers
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        def rec(prev):
            for d in range(0,10):
                actual = prev + d
                if actual > 0 and actual <= n:
                    result.append(actual)
                    rec(actual * 10)
        rec(0)
        return result
                
