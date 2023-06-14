class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Assumption: The three sum problem can be reduced to the two sum problem.
        Observation: The input array is not sorted.
               
        Let's use a hashmap to store "the third element"
        and then a double loop to compare all elements pairwise sums
        combined with a check for the third element.
        '''
