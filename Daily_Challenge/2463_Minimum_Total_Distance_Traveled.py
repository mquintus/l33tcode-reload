# 2463 - Minimum Total Distance Traveled
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        @cache
        def take_or_skip(r, f, fc):
            if r == len(robot): return 0
            if f == len(factory): return float('inf')

            # skip
            skip_steps = take_or_skip(r, f+1, 0)

            capacity = factory[f][1] - fc
            if capacity == 0: 
                return skip_steps

            # take
            steps = abs(robot[r] - factory[f][0])
            take_steps = steps + take_or_skip(r+1, f, fc+1)

            result = min(skip_steps, take_steps)
            #print(r,f,fc, result)
            return result
        return take_or_skip(0, 0, 0)
