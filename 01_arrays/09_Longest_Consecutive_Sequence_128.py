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
        - 
        '''
