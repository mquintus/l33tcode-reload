# 1751 - Maximum Number of Events That Can Be Attended II
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        startdates = [x[0] for x in events]
        n = len(events)
        dp = [[-1 for i in range(n)] for j in range(k)]

        def doSomething(i, enddate, quota):
            if quota == -1: 
                #print("No quota")
                return 0
            if i >= len(events): return 0

            if dp[quota][i] != -1:
                return dp[quota][i]

            #print ("Taking", i)
            take = -1
            if enddate < events[i][0]:
                #print("Take?")
                if dp[quota][i] != -1:
                    take = dp[quota][i]
                else:
                    take = events[i][2] 
                    if quota >= 0:
                        nextEventId = bisect.bisect_right(startdates, events[i][1])
                        take += doSomething(nextEventId, events[i][1], quota - 1)
                #print("Take?", "eventid", i, "value", take)
            #else:
            #    print("Take?", "Starts too early")
            #print ("Done Taking", i, take)

            #print ("Skipping", i)
            skip = doSomething(i+1, enddate, quota)

            #print(i, enddate, events[i][0], enddate < events[i][0], events[i][2], skip, take)
            dp[quota][i] = max(skip, take)

            return dp[quota][i]

        return doSomething(0, 0, k-1)
