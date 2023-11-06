# 1845 - Seat Reservation Manager
import heapq
class SeatManager:

    def __init__(self, n: int):
        self.free_seats = list(range(1, n+1))

    def reserve(self) -> int:
        return heapq.heappop(self.free_seats)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.free_seats, seatNumber)
        
