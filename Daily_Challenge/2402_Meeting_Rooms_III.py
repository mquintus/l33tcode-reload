# 2402 - Meeting Rooms III
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Approach:
        # There are n meeting rooms.
        # We know starting times and end times of all the meetings
        # Let's sort them
        # because the earliest starting time always has precedence.
        # i.e. when a room becomes free and a meeting is waiting and
        # another meeting is scheduled for this time, the waiting meeting
        # preceeds.
        number_of_meetings_in_room = [0]*(100) 
        free_rooms = [i for i in range(n)]
        becoming_free = []
        global maxval
        maxval = -1

        def book_room(current_room, delay=0):
            number_of_meetings_in_room[current_room] += 1
            global maxval
            maxval = max(maxval, number_of_meetings_in_room[current_room])
            heapq.heappush(becoming_free, (end+delay, current_room))

        meetings.sort()
        for start, end in meetings:
            # Case 1:
            # If a room becames free right now or has become free in the past,
            # free it now.
            # Multiple rooms can have become free.
            while becoming_free and becoming_free[0][0] <= start:
                current_room = heapq.heappop(becoming_free)[1]
                heapq.heappush(free_rooms, current_room)

            # Case 2: 
            # There is a free room. Book it.
            if free_rooms:
                current_room = heapq.heappop(free_rooms)
                book_room(current_room)
            else:
                # Case 3:
                # There is no free room.
                # This means we will free a room *in the future*
                # and book it.
                attime, current_room = heapq.heappop(becoming_free)
                delay = attime - start
                book_room(current_room, delay)
                
        
        for i, val in enumerate(number_of_meetings_in_room):
            if val == maxval:
                return i


