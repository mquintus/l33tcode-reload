class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        A two pointer challenge.

        Pick the first and the last element in the array.

        Now we loop from left and from right 
        (the lower of both)
        and see if we can improve our situation.
        (storing the maxArea value in each iteration)

        If both are equal, try changing  both at the same time.
        '''

        p = [0, len(height) - 1]

        maxArea = 0

        while p[0] <= p[1]:
            old_prod = min([height[p[0]], height[p[1]]]) * (p[1] - p[0])
            print(p[0],p[1],":",[height[p[0]], height[p[1]]], ':', old_prod)
            maxArea = max(maxArea, old_prod)
            
            if height[p[0]] >= height[p[1]]:
                p[1] -= 1
            elif height[p[0]] <= height[p[1]]:
                p[0] += 1
            else:
                p[1] -= 1
                p[0] += 1

        return maxArea


[1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1]
[1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1]
[2,3,4,5,18,17,6]
[2053, 301, 1817, 7122, 1320, 8673, 3538, 9328, 4905, 8899,1,8,6,2,5,4,8,3,7,9924,9923,9922,9921,9920,9919,9918,9917,9916,9915,9914,9913,9912,9911,9910,9909,9908,9907,9906,9905,9904,9903,9902,9901]
