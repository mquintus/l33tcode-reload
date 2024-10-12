# 2406 - Divide Intervals Into Minimum Number of Groups
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        starts = sorted([start for start,_ in intervals])
        ends = sorted([end for _,end in intervals])
        pointer_s = 0
        pointer_e = 0

        concurrent = 0
        res = 1
        while pointer_e < len(ends):
            if pointer_s < len(starts) and starts[pointer_s] <= ends[pointer_e]:
                concurrent += 1
                pointer_s += 1
                res = max(res,concurrent)
            else:
                concurrent -= 1
                pointer_e += 1
        return res
