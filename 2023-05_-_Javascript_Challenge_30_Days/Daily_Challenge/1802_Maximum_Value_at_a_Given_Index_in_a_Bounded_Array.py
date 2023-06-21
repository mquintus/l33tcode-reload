class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        '''
        There are two factors that can make moving a number expensive:
        - if it is far away from all the other numbers.
        - if its cost is high.

        The brute force approach is to calculate moving all other numbers j!=i
        for each number i.
        Doesn't scale though, we need to pre-select.

        The candidates for the target value are ...
        those with the highest cost
        those far from the median
        '''      
        most_expensive = sorted(zip(cost, nums))
        candidates = list(list(zip(*most_expensive[-20:]))[1])

        # These candidates are not good enough.
        # Better to weigh numbers by locality and weight 
        # Just to think
        # If there are a million ""light"" elements at position zero
        # and just one heavy element (weight 1000) at position 10,
        # moving the million lightweight elements to the heavy element
        # will cost 10 million while moving the heavy element will only 
        # cost 10 thousand.
        # Therefore: If we add up all numbers times their weight, divide by the accumulated weight
        # then we end up close to the "most heavy" position.
        weighted_nums = [i * c for i,c in most_expensive]
        weighted_average = sum(weighted_nums) / sum(cost)
        #print(weighted_average)
        distance = [abs(i - weighted_average) for i in nums]
        far_numbers_zipped = sorted(zip(distance, nums))
        far_numbers = list(zip(*far_numbers_zipped))[1]
        #
        # The question is, how many numbers to we need to test?
        # Maybe 20% ?
        #

        #
        # Let's try something else.
        # Binary search.
        # The problem here is that we need an array without local minima
        # In fact: The problem doesn't have local minima.
        min_movements = float('inf')
        bestBestNum = -1
        bin_start = min(nums)
        bin_end = max(nums) + 1
        while bin_start < bin_end:
            bin_mid = bin_start + (bin_end-bin_start)//2
            guessedNum = bin_mid
            a = sum([abs(nums[i] - (guessedNum - 1)) * cost[i] for i in range(len(nums))])
            b = sum([abs(nums[i] - (guessedNum)) * cost[i] for i in range(len(nums))])
            if a > b:
                bin_start = bin_mid + 1
            else:
                bin_end = bin_mid

            min_movements = min(min_movements, b)

        return min_movements
            
