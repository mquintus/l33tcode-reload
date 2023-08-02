class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def solve(nums, indexes):
            if len(indexes) == len(nums):
                return [[]]
            results = []
            for i in nums:
                if i not in indexes:
                    extensions = solve(nums, indexes + [i])
                    for e in extensions:
                        result = [i]
                        result.extend(e)
                        results.append(result)
            return results
        
        return solve(nums, [])
