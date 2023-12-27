# 1578 - Minimum Time to Make Rope Colorful
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        '''
        Intuition:
        - check if there are consequtive balloons
        - if so, keep only that one balloon with the highest score
        '''
        n = len(colors)
        cost = 0
        prev_color = "*"
        first_index = -1
        for p, curr_color in enumerate(colors):
            if curr_color == prev_color:
                continue

            if p != first_index + 1:
                cost += (sum(neededTime[first_index:p]) - max(neededTime[first_index:p]))

            prev_color = curr_color
            first_index = p

        p += 1
        #print(p, first_index)
        if p != first_index + 1:
            cost += (sum(neededTime[first_index:p]) - max(neededTime[first_index:p]))

            
        return cost
