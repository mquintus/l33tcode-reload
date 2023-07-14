class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        '''
        Hashtable solution:       
        '''
        hashmap = {}
        max_sequence = 0
        for el in arr:
            if el - difference in hashmap:
                hashmap[el] = hashmap[el - difference] + 1
            else:
                hashmap[el] = 1
            max_sequence = max(max_sequence, hashmap[el])
        return max_sequence
