# 3016 - Minimum Number of Pushes to Type Word II
class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        curr_space = 8
        curr_length = 1
        result = 0
        for occ, val in sorted([[o,v] for v,o in counter.items()])[::-1]:
            result += occ * curr_length
            curr_space -= 1
            if curr_space == 0:
                curr_space = 8
                curr_length += 1
        return result
