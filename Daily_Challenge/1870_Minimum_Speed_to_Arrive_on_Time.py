class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        def get_travel_time(speed):
            tt = 0
            for d in dist[:-1]:
                tt += ceil(d / speed)
            tt += dist[-1] / speed
            return tt
        
        start = 1
        end = 10**9

        if hour < len(dist) - 1:
            return -1

        solution = end + 1
        while start < end:
            mid = (start + end) // 2

            tt = get_travel_time(mid)
            if tt > hour:
                start = mid + 1
            elif tt <= hour:
                solution = min(solution, mid)
                end = mid
        
        if solution == end + 1:
            solution = -1
        return solution
