# 2009 - Minimum Number of Operations to Make Array Continuous
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        '''
        Interesting question.

        Let's try a sliding window approach.
        We count how many matches we've got inside
        the sliding window.

        This requires us to first sort the array.
        Then we find the largest window that has a max distance of n
        and count how many distinct elements 'd' are inside the window.

        The solution is n - d
        '''
        nums = sorted(nums)
        n = len(nums)

        if n <= 1:
            return 0

        p1 = 0
        p2 = 1
        counter = {nums[p1]: 1}
        max_counter = 1
        curr_counter = 1
        if nums[p2] not in counter:
            counter[nums[p2]] = 0
            if nums[p2] - nums[p1] < n:
                max_counter += 1
                curr_counter += 1
        counter[nums[p2]] += 1

        while p2 < n - 1:
            p2 += 1
            while nums[p2] - nums[p1] >= n:
                counter[nums[p1]] -= 1
                if counter[nums[p1]] == 0:
                    curr_counter -= 1
                p1 += 1
            if nums[p2] - nums[p1] < n:
                if p2 >= n:
                    break
                if nums[p2] not in counter or counter[nums[p2]] == 0:
                    counter[nums[p2]] = 0
                    curr_counter += 1
                counter[nums[p2]] += 1
            max_counter = max(max_counter, curr_counter)
        return n - max_counter
            


