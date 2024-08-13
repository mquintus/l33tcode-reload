# 40 - Combination Sum II
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        solutions = set()

        def take_or_skip(i, currsum, values):
            if currsum == target:
                solutions.add(tuple(sorted(values)))
                return

            if currsum > target:
                return
            
            if i >= n:
                return

            # take 
            if currsum+candidates[i] <= target:
                values.append(candidates[i])
                take_or_skip(i+1, currsum+candidates[i], values)
                values.pop()

            # skip
            while i < n - 1 and candidates[i] == candidates[i+1]:
                i += 1
            take_or_skip(i+1, currsum, values)

        take_or_skip(0, 0, [])
        return list(solutions)
