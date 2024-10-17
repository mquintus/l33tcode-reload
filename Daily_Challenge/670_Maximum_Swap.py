# 670 - Maximum Swap
class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [int(el) for el in str(num)]

        upperlimit = 10

        while True:
            maxvalue = -1
            found_better_max = False
            for pointer, val in enumerate(nums):
                if val >= maxvalue and val < upperlimit:
                    maxvalue = val
                    maxpointer = pointer
                    found_better_max = True
            if not found_better_max:
                break
            #print(maxpointer, maxvalue)

            leftpointer = 0
            while leftpointer < maxpointer and nums[leftpointer] >= maxvalue:
                leftpointer += 1
            if leftpointer == maxpointer:
                upperlimit = maxvalue
            else:
                #print(maxpointer, maxvalue, leftpointer, nums[leftpointer])
                nums[leftpointer], nums[maxpointer] = nums[maxpointer], nums[leftpointer]
                break
        return int("".join([str(el) for el in nums]))

