# 763 - Partition Labels
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        c = Counter(s)

        cuts = []

        incomplete_count = 0
        lc = {}
        i = 0
        for el in s:
            i += 1
            if el not in lc:
                lc[el] = 0
                incomplete_count += 1
            lc[el] += 1
            if lc[el] == c[el]:
                incomplete_count -= 1
                if incomplete_count == 0:
                    cuts.append(i)
                    i = 0
        

        return cuts
