# 621 - Task Scheduler
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        counter = Counter(tasks)

        maxcount = cycles = sorted(counter.values())[-1]
        taskcount = len(tasks)

        how_many_maxcounts = sum([1 for x in counter.values() if x == maxcount])

        estimate = max((cycles-1) * (n+1) + how_many_maxcounts, taskcount)
        #print(how_many_maxcounts,(cycles-1) * (n+1), taskcount)

        return estimate
