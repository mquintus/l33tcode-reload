class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        '''
        Since the limit of the numbers is 0 to 500,
        a hashmap / list of numbers seems to be a possibility.

        This is not a 1st degree math problem, because the numbers are irrelevant,
        only their relative distances are important.

        We will use a hashmap for every found distance between 
        two nodes.

        If a left node is actually a right node of a previous iteration,
        add up the previous length.
        '''

        # edge case when there are only two numbers present:
        # they are an algorithmic sequence.
        if len(nums) == 2:
            return 2

        
        allNums = {}

        #
        # Another edge case: distance = 0        
        zero_distance = [0 for i in range(501)]

        maxSteps = 0
        for i, lower in enumerate(nums):
            zero_distance[lower] += 1
            maxSteps = max(maxSteps, zero_distance[lower] - 1)
            for j, higher in enumerate(nums[i+1:]):
                j = j + i + 1
                distance = higher-lower
                if distance == 0:
                    continue
                if lower not in allNums.keys():
                    allNums[lower] = {}
                if higher not in allNums.keys():
                    allNums[higher] = {}
                if distance not in allNums[lower].keys():
                    allNums[lower][distance] = 0

                allNums[higher][distance] = allNums[lower][distance] + 1
                maxSteps = max(maxSteps, allNums[higher][distance])

        
        return maxSteps + 1


