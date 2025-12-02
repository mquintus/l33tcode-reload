# 3623 - Count Number of Trapezoids I
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 1_000_000_007

        points_by_y = dict()
        for x,y in points:
            if y not in points_by_y:
                points_by_y[y] = 0
            points_by_y[y] += 1

        total = 0

        to_remove = list()
        for y, count in points_by_y.items():
            if count < 2:
                to_remove.append(y)

        while to_remove:
            del points_by_y[to_remove.pop()]


        pairwise_sorted = sorted(list(points_by_y.items()))

        prev = 0
        for y, n in pairwise_sorted:
            ways = (n * (n-1))//2
            if ways == 0: continue
            total += prev*ways
            prev += ways
            
                
        
        return total % MOD
                

