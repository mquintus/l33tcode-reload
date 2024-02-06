# 49 - Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            counter = frozenset(Counter(s).items())
            if counter not in anagrams.keys():
                anagrams[counter] = []
            anagrams[counter].append(s)
        return anagrams.values()

