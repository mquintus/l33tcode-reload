# 739 - Daily Temperatures
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Let's iterate from the end
        '''

        result = []
        monotonicStack = []
        for i in range(len(temperatures)-1, -1, -1 ):
            el = temperatures[i]

            while len(monotonicStack) > 0 and el >= monotonicStack[0][0]:
                monotonicStack.pop(0)

            if len(monotonicStack) == 0:
                distance = 0
                result.insert(0, distance)
                monotonicStack.insert(0, (el, i))
                continue
            
            if el < monotonicStack[0][0]:
                distance = monotonicStack[0][1] - i
                result.insert(0, distance)
                monotonicStack.insert(0, (el, i))
            
        return result


