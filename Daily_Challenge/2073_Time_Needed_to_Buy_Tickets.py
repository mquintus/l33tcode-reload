# 2073 - Time Needed to Buy Tickets
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        seconds = 0
        newlist = []
        n = len(tickets)
        i = -1
        while True:
            i = (i + 1) % n
            if tickets[i] == 0:
                continue

            tickets[i] -= 1
            seconds += 1

            if i == k and tickets[i] == 0:
                return seconds
