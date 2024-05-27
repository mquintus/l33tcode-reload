# 1608 - Special Array With X Elements Greater Than or Equal X
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l = 0
        counter = len(nums)+1

        while counter >= l:
            #print(l)
            counter = 0
            for i in nums:
                if i >= l:
                    counter += 1
            if counter == l:
                return counter
            l += 1
        return -1
