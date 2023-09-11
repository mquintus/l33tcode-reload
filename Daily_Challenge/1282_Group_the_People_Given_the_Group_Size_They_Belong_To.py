class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = [[] for _ in range(501)]

        for i, g in enumerate(groupSizes):
            if len(groups[g]) == 0 or len(groups[g][-1]) == g:
                groups[g].append([])
            if len(groups[g][-1]) < g:
                groups[g][-1].append(i)

        flat_groups = []
        for g in groups:
            flat_groups.extend(g)

        return flat_groups
