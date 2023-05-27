class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        Naive idea: 
        Take the first element and check if it is still in the list.
        otherwise iterate to the next element and check if it is in the right part of the list.
        Time complexity: O(n^2)
        Space complexity: O(1)
        '''
        def iterative(nums: List[int]) -> bool:
            for pos, val in enumerate(nums):
                print(pos, val)
                if val in nums[pos+1:]:
                    return True
            return False
        # return iterative(nums)

        '''
        Alternative idea: 
        Recursive approach to pop the first element and check if it still in the list,
        otherwise recursively do the check on the remaining (popped) list.
        Time complexity: O(n^2)
        Space complexity: O(1)
        but worse by a constant factor to handle the recursive context change.
        '''
        def recursive(nums: List[int]) -> bool:
            if len(nums) == 0:
                return False
            first = nums.pop()
            if first in nums:
                return True
            return recursive(nums)
        # return recursive(nums)

        '''
        Since the list is not ordered, finding an element can't be quicker than O(n)
        and since we've got to do this for each element, the time complexity is always quadratic.

        Next idea: Using a hashmap of length n.

        Time Complexity: O(n)
        Space Complexity O(n)

        We loop through the list once (O(n)) and add each element to the hashtable / hashmap 
        Storing and checking in a hashtable requires only (O(1)) 

        Note that the time complexity of the hashtable lookup can increase to O(n) in the worst case
        if all items land in the same bucket. In our leetcode example that would happen if 
        the list contains [0, n, 2n, 3n, 4n, ...] as values with a list of lenght n.
        In this corner case, the hashtable time complexity would degenerate to O(n^2) as the previous solutions were,
        but with far worse space complexity. 
        In a real world environment, 
        this could be improved by:
        - instead of modulo based hashtable, using a proper hashing scheme 
        - if many collisions occur, increase the key space / length of the hashtable
          - also consider adding a second hasing scheme (as bloom filters do)
        '''
        class naive_hashtable:
            def __init__(self, size):
                self.size = size
                self.entries = 0
                self.table = [None for i in range(size)]
            def put(self, item):
                if self.entries == self.size:
                    return False
                pos = item % self.size
                while self.table[pos] is not None and self.table[pos] != item:
                    pos = (pos + 1) % self.size
                if self.table[pos] is None:
                    self.entries += 1
                    self.table[pos] = item
                return True
            def has(self, item):
                if self.entries == 0:
                    return False
                tries = self.size
                pos = item % self.size
                while self.table[pos] != item:
                    if self.table[pos] is None or tries == 0:
                        return False
                    pos = (pos + 1) % self.size
                    tries -= 1
                return self.table[pos] == item

        def use_hastable(nums: List[int]) -> bool:
            size = len(nums)
            hashtable = naive_hashtable(size)
            for val in nums:
                if hashtable.has(val):
                    print("Match")
                    return True
                hashtable.put(val)
            return False
            
        return use_hastable(nums)
