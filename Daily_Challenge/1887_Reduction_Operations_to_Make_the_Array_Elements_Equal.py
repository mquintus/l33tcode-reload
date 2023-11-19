# 1887 - Reduction Operations to Make the Array Elements Equal
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # Intuition
        #
        # Each existing value represents a step.
        # We need to know, how many of these exist.
        # How many steps, and how many items per step.
        #
        # Approach
        # 
        # A) We add the number of steps as the number of the highest step. 
        # B) The next highest step is going to be increased by the number of the highest step.
        # C) Iterate until finished.
        #
        # Time complexity: Since a type of sorting is required, it is O(n log n)
        # Space complexity: We will store a dict with each unique number as the keys and their count as the value
        # with in the worst case is O(n)
        #
        # Pseudo-Code
        # 
        # Create a count for all elements (in linear time)
        # Create a max heap (n * log n)
        # Loop the max heap (n)
        #     get highest step (1)
        #     pop highest step (log n)
        #     Increase counter by number if highest step
        #     get now-highest step (1)
        #     Increase number of second-highest step in hashmap
        # return counter

        myHashmap = {}
        myMaxHeap = []

        for item in nums:
            if item not in myHashmap:
                myHashmap[item] = 0
                heapq.heappush(myMaxHeap, -1 * item)
            myHashmap[item] += 1
        
        operations = 0

        count = 0
        while len(myMaxHeap) > 1:
            step = -1 * heapq.heappop(myMaxHeap)
            count = myHashmap[step] + count
            operations += count

        return operations


        
