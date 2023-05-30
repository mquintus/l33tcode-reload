import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Naive approach: 
        1. Create a counter for each string
        2. Compare counters: All counters that are identical belong together
        '''
        myCounters = {}

        for myString in strs:
            # It is necessary to sort the myString because collections.Counter
            # preserves order. I am still looking for a real hashmap (where the order is determined by the key)
            hashed = str(collections.Counter(sorted(myString)))
            if hashed not in myCounters.keys():
                myCounters[hashed] = []
            myCounters[hashed].append(myString)

        return myCounters.values()
