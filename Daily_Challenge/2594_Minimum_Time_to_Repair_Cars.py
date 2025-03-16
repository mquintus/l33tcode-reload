# 2594 - Minimum Time to Repair Cars
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        price_of_next = [(1 * r, 1, r, p) for p,r in enumerate(ranks)]
        amounts = [0]* len(ranks)
        times = [0]* len(ranks)
        heapq.heapify(price_of_next)
        time = 0
        for i in range(cars, 0, -1):
            price, new_amount, rank, pos = heapq.heappop(price_of_next)
            amounts[pos] = new_amount
            time = max(time, price)
            new_amount += 1
            heapq.heappush(price_of_next, (rank*new_amount*new_amount, new_amount, rank, pos))
            times[pos] = price

        return time
