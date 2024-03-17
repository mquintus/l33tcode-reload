# 57 - Insert Interval
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newResult = []
        inserted = False
        rememberStart = None
        rememberEnd = newInterval[1]
        
        for start, end in intervals:
            if inserted == True:
                newResult.append([start, end])
                continue

            if rememberStart is not None:
                if start > rememberEnd:
                    newResult.append([rememberStart, rememberEnd])
                    newResult.append([start, end])
                    inserted = True
                elif start == rememberEnd:
                    newResult.append([rememberStart, end])
                    inserted = True
                elif end < rememberEnd:
                    pass
                elif end == rememberEnd:
                    newResult.append([rememberStart, rememberEnd])
                    inserted = True
                elif end >= rememberEnd:
                    rememberEnd = end
                    newResult.append([rememberStart, rememberEnd])
                    inserted = True
                else:
                    rememberEnd = end
                continue

            if rememberStart is None:
                if end < newInterval[0]:
                    newResult.append([start, end])
                elif start > rememberEnd:
                    newResult.append(newInterval)
                    newResult.append([start, end])
                    inserted = True
                elif start <= newInterval[0] and end >= rememberEnd:
                    newResult.append([start, end])
                    inserted = True
                elif newInterval[0] <= start and end >= rememberEnd:
                    rememberStart = newInterval[0]
                    rememberEnd = end
                elif start <= newInterval[0] and rememberEnd >= end:
                    rememberStart = start

        if not inserted:
            if rememberStart is None:
                rememberStart = newInterval[0]
            newResult.append([rememberStart, rememberEnd])

        return newResult
