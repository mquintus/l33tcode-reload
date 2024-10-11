# 1942 - The Number of the Smallest Unoccupied Chair
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        chairs = list(range(len(times)))

        events = []
        for index, (arrive, left) in enumerate(times):
            heapq.heappush(events, (arrive, left, index))
        
        while events:
            time, ev, person = heapq.heappop(events)
            #print(time, ev, person)
            if ev != float('-inf'):
                chair = heapq.heappop(chairs)
                #print("At",time,"person",person,"gets chair",chair)
                if person == targetFriend:
                    return chair
                heapq.heappush(events, (ev, float('-inf'), chair))
                #print(events)
            else:
                #print("At",time,"chair",person,"is abandoned")
                heapq.heappush(chairs, person)


