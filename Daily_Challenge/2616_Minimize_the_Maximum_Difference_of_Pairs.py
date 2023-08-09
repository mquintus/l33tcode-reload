class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        '''
        Let's sort nums

        '''
        
        nums.sort()

        differences = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
        differences.sort()

        start = 0
        end = nums[-1] - nums[0] + 1

        while start < end:
            threshold = start + (end - start) // 2

            i = 0
            c = 0
            while i < len(nums) - 1:
                if differences[i] <= threshold:
                    c += 1
                    i += 1
                i += 1

            if c >= p:
                end = threshold
            elif c < p:
                start = threshold + 1
                
        return start
