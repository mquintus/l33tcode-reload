# 1310 - XOR Queries of a Subarray
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        left = [0]
        for el in arr:
            left.append(left[-1]^el)
      
        result = []
        for fr, to in queries:
            result.append(left[fr]^left[to+1])
        return result
