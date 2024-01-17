# 1207 - Unique Number of Occurrences
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequencies = Counter(arr)
        frequencies_of_frequencies = Counter(frequencies.values())
        for f in frequencies_of_frequencies.values():
            if f != 1:
                return False
        return True
