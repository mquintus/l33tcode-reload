class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Naive solution:
        Pop an element from the list and search for the "complement" in the remaining list.
        Worst case time complexity: O(n^2)
        '''
        def naive_solution(nums: List[int], target: int) -> List[int]:
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if target - nums[i] == nums[j]:
                        return i,j
        # return naive_solution(nums, target)

        '''
        Bucket sort solution: (hash map)
        Since we are already looping once through the whole list,
        we might use this loop to save the item to a hashmap.
        Adding something to a hashmap or into a bucket has a time complexity of O(1)
        
        At the same time, for each num, we calculate the complement (O(1)) and
        we check if the complement is already in the bucket (O(1))

        At the time when the last num ends up in the bucket, checking the hashmap 
        will definitely return the index of complement.

        Time complexity: O(n)
        Space complexity: O(n)
        '''
        def bucket_sort_solution(nums: List[int], target: int) -> List[int]:
            hashmap = {}
            for i in range(len(nums)):
                complement = target - nums[i]
                if complement in hashmap.keys():
                    return hashmap[complement], i
                hashmap[nums[i]] = i
        return bucket_sort_solution(nums, target)
