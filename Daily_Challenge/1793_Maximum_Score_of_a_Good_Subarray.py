# 1793 - Maximum Score of a Good Subarray
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pi = k
        pj = k
        
        def addElementAndCalculate(minElement, newIndex, i, j):
            minElement = min(minElement, nums[newIndex])
            return min(minElement, nums[newIndex]) * (j - i + 1)

        min_element = nums[k]
        score = addElementAndCalculate(min_element, k, pi, pj)
        max_score = score

        while pi > 0 or pj < n - 1:
            score_move_right = 0
            if pj < n - 1:
                score_move_right = addElementAndCalculate(min_element, pj + 1, pi, pj + 1)
            score_move_left = 0
            if pi > 0:
                score_move_left = addElementAndCalculate(min_element, pi - 1, pi - 1, pj)
            if score_move_right > score_move_left or (pi == 0 and pj < n - 1):
                pj += 1
                new_element = nums[pj]
                score = score_move_right
            elif score_move_right <= score_move_left or (pi > 0 and pj == n - 1):
                pi -= 1
                new_element = nums[pi]
                score = score_move_left
            
            min_element = min(min_element, new_element)
            if score > max_score:
                max_score = score 

        return max_score


