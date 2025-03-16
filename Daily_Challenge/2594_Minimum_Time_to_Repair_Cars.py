# 2594 - Minimum Time to Repair Cars
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def is_possible(time):
            #print("Is it possible in", time)
            n = cars
            for r in ranks:
                a = int((time // r)**0.5)
                n -= a
                #print(f"Rank {r} repaired {a} cars, {n} remaining")
                if n <=0 : return True
            return False

        start = 0
        end = cars*cars*max(ranks)
        while start <= end:
            mid = (start + end) // 2
            ip = is_possible(mid)
            if ip:
                if not is_possible(mid-1):
                    return mid
                end = mid
            else:
                start = mid + 1
