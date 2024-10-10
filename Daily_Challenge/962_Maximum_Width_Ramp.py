# 962 - Maximum Width Ramp
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        monoStack = []
        maxl = 0
        for i, el in enumerate(nums):
            #while len(monoStack) > 0 and monoStack[-1][0] > el:
            #    monoStack.pop()
            #    
            if len(monoStack) == 0 or el < monoStack[-1][0]:
                monoStack.append((el, i))

        print(monoStack)
        for i in range(len(nums)-1, -1, -1):
            if len(monoStack) == 0:
                break
            el = nums[i]
            while len(monoStack) > 0 and monoStack[-1][0] <= el:
                comp = monoStack.pop()
                #print(comp)
                maxl = max(i - comp[1], maxl)


        return maxl
