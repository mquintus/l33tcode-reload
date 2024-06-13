# 2037 - Minimum Number of Moves to Seat Everyone
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        return sum([abs(seats[i] - students[i]) for i in range(len(seats))])
