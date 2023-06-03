class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Naive approach:
        - We iterate each element and put that number into a bucket.
        - For each bucket, we store beginning and end
          - If the number is between beginning and end, do nothing
          - If the number is adjacent, increase the counter associated with the bucket and update beginning/end
        - Merging buckets "after the fact" is expensive: What to do about (1,2,3, 5,6,7, 4)???
        - Problem: in the worst case, we get a distinct bucket per element

        Idea: Do sorting, minheaps, etc... 
        Problem: Requirement is O(n) time complexity.

        Back to the naive approach:
        - Merging buckets maybe isn't too expensive. Even if the expense is n, we come out with two n of executing
          which is still O(n)
        - but... simpler. Forget about beginning/end. 

        Algorithm outline:
        - We iterate each element and hash that number:  n steps.
        - We iterate each element a second time and check if it is a "begin" element by checking if i - 1 is in the hash map.
          - This takes 2*n checks, one for each number, one for each "before number"
        - If it is a begin element, iteratively check the after element until not found in the hashmap 
          -> takes at most n*1 checks if not consequtive and 1*n checks if totally consequtive 
        - Keep track of chain length -> return
        '''
        hashmap = {}
        for num in nums:
            hashmap[num] = 1
        
        global_max = 0
        for num in nums:
            local_max = 1
            if num - 1 not in hashmap:
                while num + 1 in hashmap:
                    local_max += 1
                    num += 1
            if local_max > global_max:
                global_max = local_max
        return global_max

        
