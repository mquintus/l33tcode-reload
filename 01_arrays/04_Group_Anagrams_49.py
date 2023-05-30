
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Naive approach: 
        1. Create a counter for each string
        2. Compare counters: All counters that are identical belong together

        Ideas for optimizing: (not implemented)
        - Since the alphabet is restricted to 26 letters (lowercase),
        the Counter could be a highly optimized hashmap
        - Breadth-first-search parsing all strings in parallel might yield performance advantages (just guessing)
        '''

        def counters_approach(strs: List[str]) -> List[List[str]]:
            import collections
            myCounters = {}

            for myString in strs:
                # It is necessary to sort the myString because collections.Counter
                # preserves order. I am still looking for a real hashmap (where the order is determined by the key)
                hashed = str(collections.Counter(sorted(myString)))
                if hashed not in myCounters.keys():
                    myCounters[hashed] = []
                myCounters[hashed].append(myString)

            return myCounters.values()
        # return counters_approach(strs)

        ''' 
        Sorted string approach:
        Looking at some other solutions, I realized that sorting and then counting
        if not better than just sorting and using the sorted string directly as the hash.
        '''
        def sort_approach(strs: List[str]) -> List[List[str]]:
            myCounters = {}
            for myString in strs:
                hashed = "".join(sorted(myString))
                if hashed not in myCounters.keys():
                    myCounters[hashed] = []
                myCounters[hashed].append(myString)
            return myCounters.values()
        return sort_approach(strs)
