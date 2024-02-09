# 368 - Largest Divisible Subset
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        bestsolution = [(-1, -1)]
        nums.sort()
        length = 1
        highest = 0
        dp = [1] * (len(nums) + 2)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > length:
                        length = dp[i]
                        highest = i

        #print(length, highest)

        final_solution = [[]]

        def get_solution(i, highest, subset, length):
            #print("len(subset), length", len(subset), length)
            if i == -1:
                #print('Win')
                final_solution[0] = subset
                return 

            if i == len(nums):
                return

            el = nums[i]

            if highest % el != 0 or dp[i] != length:
                skip = get_solution(i-1, highest, subset, length)
                return 
            #print(el, length, highest, len(subset), subset)
            take = get_solution(i-1, el, [el, *subset], length-1)

        get_solution(len(nums) - 1, nums[highest], [], length)

        return final_solution[0]
