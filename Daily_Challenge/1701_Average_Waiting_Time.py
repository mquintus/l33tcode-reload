# 1701 - Average Waiting Time
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        busyUntil = 0
        overallWaitingTime = 0
        for arrival, difficulty in customers:
            waitingTime = difficulty
            if busyUntil > arrival:
                waitingTime += busyUntil - arrival
            busyUntil = max(arrival, busyUntil) + difficulty
            #print(waitingTime)
            overallWaitingTime += waitingTime
        return overallWaitingTime / len(customers)
