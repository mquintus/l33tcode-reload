# 2044 - Count Number of Maximum Bitwise-OR Subsets
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Intuition: OR can only ever increase.
        # Therefore the whole array OR has the maximum.
        # Maybe the first and last are most significant
        # 3 0 0 0 0 0 0 0 4
        # then the answer is: only the whole array
        # or the highest numbers are grouped together
        # 0 0 0 3 4 0 0 0 0 
        # then including anything else is optional but those two numbers
        # whereas the case where all numbers are subbits of the main number
        # 1 1 3 1 1 
        # requires us to count all subsets that include the 3
        #
        #
        # We can try sliding window, but itself only gives a subset of the solution
        # [1] 3  3  1
        # [1  3] 3  1
        #    [3] 3  1
        #    [3  3] 1
        #       [3] 1
        #       [3  1]
        # doesnt find all subsets
        # e.g. 3 3 1 and the whole array
        #
        #
        # Thus, we want to use sliding window to find the minimal subsets
        # and then extend those to "beginning" and "end"
        # 1  1 [3] 3  1
        # 1  1  3 [3] 1
        # but how do we avoid duplicates?
        #
        # Looking at the constraints. Only 16 numbers. That allows for
        # slow solutions.
        # Comments say it's only backtracking. 
        # WTF
        #
        highest = reduce(operator.or_, nums)
        def backtrack(i, val):
            nonlocal highest
            # abort
            if i >= len(nums): return 0
            # skip
            subsetcount = backtrack(i+1, val)
            # take
            val |= nums[i]
            if val == highest:
                subsetcount += (2**(len(nums)-i-1))
                # Good news: We know that all following subsets have to be counted
                # and there is a formula, so let's shorten this
            else:
                subsetcount += backtrack(i+1, val)
            return subsetcount
        return backtrack(0,0)
