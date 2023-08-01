class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        First we order all the intervals by start and end.
        Then we consider only those who actually overlap
        and of any two that overlap, the one that end last gets removed

        '''

        def overlaps(a,b):
            return a[0] < b[1] and a[1] > b[0]

        intervals.sort()

        i = 0
        j = 1
        removed = 0
        while i < len(intervals):
            j = i + 1
            
            if j == len(intervals):
                break

            if overlaps(intervals[i], intervals[j]):
                if intervals[j][1] < intervals[i][1]:
                    del intervals[i]
                    removed += 1
                    continue
                else:
                    del intervals[j]
                    removed += 1
                    continue
            else:
                i += 1

        return removed
