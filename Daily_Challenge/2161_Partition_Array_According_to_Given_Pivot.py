# 2161 - Partition Array According to Given Pivot
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a = []
        b = 0
        c = []
        for el in nums:
            if el < pivot:
                a.append(el)
            elif el > pivot:
                c.append(el)
            else:
                b += 1
        return [*a, *([pivot]*b), *c]
