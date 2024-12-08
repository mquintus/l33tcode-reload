# 2054 - Two Best Non-Overlapping Events
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        #print(events)
        n = len(events)
        bestsum = max([v for _,_,v in events])

        by_enddate = [(e,v) for s,e,v in events]
        by_enddate.sort()
        by_enddate_map = {}

        bestval_by_enddate = 0
        for e,v in by_enddate:
            bestval_by_enddate = max(bestval_by_enddate, v)
            by_enddate_map[e+1] = bestval_by_enddate
        by_enddate_list = list(by_enddate_map.items())
        #print(by_enddate_list)

        # the 0th event can't match with any preceeding events
        for i in range(1,n):
            s1,e1,v1 = events[i]
            
            index_best_val_per_startdate = bisect.bisect_right(by_enddate_list, (s1,))
            #print("Starting at", s1, "Bisect index",index_best_val_per_startdate)
            #print(events[i], "pre-matches", by_enddate_list[index_best_val_per_startdate])
            e,v = by_enddate_list[index_best_val_per_startdate]
            while index_best_val_per_startdate >= 0 and e > s1:
                #print("in loop",index_best_val_per_startdate, e, s1)
                index_best_val_per_startdate -= 1  
                e,v = by_enddate_list[index_best_val_per_startdate]
            if index_best_val_per_startdate < 0 or e > s1:
                #print(index_best_val_per_startdate, e, s1)
                #print("No match")
                continue
            e,v = by_enddate_list[index_best_val_per_startdate]
            #print(events[i], "matches", by_enddate_list[index_best_val_per_startdate])

            bestsum = max(bestsum, v1+v)
        return bestsum

