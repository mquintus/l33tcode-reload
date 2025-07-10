# 3440 - Reschedule Meetings for Maximum Free Time II
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        startTime.sort()
        endTime.sort()

        #print(startTime, endTime)

        breaks = []
        breaks.append(startTime[0])
        #print("Meeting",0,"starts at", startTime[0], "which gives a break of", startTime[0])
        for i in range(1,len(startTime)):
            #print("Meeting",i,"starts at", startTime[i], "and meeting", i-1, "ended at", endTime[i-1],"which gives a break of", startTime[i] - endTime[i-1])
            breaks.append(startTime[i] - endTime[i-1])
        breaks.append(eventTime -  endTime[-1])

        #print(breaks)

        largest_break_after = [0]
        largest_break_before = [0]

        n = len(startTime)
        for i in range(0,n-1):
            #print("i",i,"breaks[i]",breaks[i])
            largest_break_before.append(max(breaks[i], largest_break_before[-1]))
            largest_break_after.append(max(breaks[n-i], largest_break_after[-1]))
        #largest_break_after.append(0)
        #largest_break_after.append(0)
        largest_break_after = largest_break_after[::-1]
        #print("largest_break_before",largest_break_before)
        #print("largest_break_after",largest_break_after)

        best_result = 0
        # Check 1 - can I put a meeting somewhere else?
        for meeting in range(len(startTime)):
            length_of_meeting = endTime[meeting] - startTime[meeting]
            break_before = breaks[meeting]
            break_after = breaks[meeting+1]
            #print("* meeting",meeting,"largest_break_after[meeting]",largest_break_after[meeting],"largest_break_before[meeting]",largest_break_before[meeting],"length_of_meeting",length_of_meeting)
            #print("break_before",break_before,"break_after",break_after)
            if largest_break_after[meeting] >= length_of_meeting or largest_break_before[meeting] >= length_of_meeting:
                best_result = max(best_result, break_before+break_after+length_of_meeting)
                #print("It's possible to move meeting",meeting,"with length",length_of_meeting,"into a gap of either",largest_break_before[meeting], "or",  largest_break_after[meeting])
                #print("to combine breaks of",break_before, "and",  break_after, "and get to ***",break_before+break_after+length_of_meeting)
            else:
                best_result = max(best_result, break_before+break_after)
                #print("It's possible to move meeting",meeting,"to the side to combine breaks of",break_before, "and",  break_after)
                #print("and get to ***",break_before+break_after)



        return best_result


