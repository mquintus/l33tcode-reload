# 1637 - Widest Vertical Area Between Two Points Containing No Points
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # Intuition:
        # The y values are not relevant.
        # The question is, given two points where no other point is in between,
        # what is the max distance between any points i!=j
        x_values = sorted([x[0] for x in points])

        distance = -1
        prev = x_values[0]       
        for x in x_values[1:]:
            distance = max(distance, x - prev)
            prev = x
        
        return distance
