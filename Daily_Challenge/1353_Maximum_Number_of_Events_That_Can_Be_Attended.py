# 1353 - Maximum Number of Events That Can Be Attended
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        starts = [a for a,b in events]
        left = min(starts)

        ends = [b for a,b in events]
        right = max(ends)

        events.sort()

        available_enddates = []

        count = 0
        i = 0
        for day in range(left, right+1):
            #print("Day",day)
            while i < len(events) and events[i][0] <= day and events[i][1] >= day:
                heapq.heappush(available_enddates, events[i][1])
                i += 1
            #print("available_enddates",available_enddates)
            if len(available_enddates) == 0:
                continue
            enddate = 0
            while available_enddates and enddate < day:
                enddate = heapq.heappop(available_enddates)
            #print("available_enddates",available_enddates)
            if enddate >= day:
                count += 1

        return count
