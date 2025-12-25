# 3074 - Apple Redistribution into Boxes
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort()
        total = 0
        apple = sum(apple)
        while apple > 0:
            total += 1
            if capacity[-1] >= apple:
                break
            apple -= capacity.pop()

            
        return total
