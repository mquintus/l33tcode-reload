# 3439 - Reschedule Meetings for Maximum Free Time I
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        startTime.sort()
        endTime.sort()

        #print(startTime, endTime)

        breaks = []
        breaks.append(startTime[0])
        for i in range(1,len(startTime)):
            #print("Meeting",i,"starts at", startTime[i], "and meeting", i-1, "ended at", endTime[i-1],"which gives a break of", startTime[i] - endTime[i-1])
            breaks.append(startTime[i] - endTime[i-1])
        breaks.append(eventTime -  endTime[-1])

        maxBreak = 0
        maxBreak = currSum = sum(breaks[:k+1])
        #print(breaks, currSum)
        for i in range(k, len(breaks)-1):
            #print("i", i, currSum)
            currSum -= breaks[i - k]
            currSum += breaks[i+1]
            #print("i", i, "new currSu",currSum)
            maxBreak = max(maxBreak, currSum)
            #print("i", i, maxBreak)
        
        return maxBreak
        
