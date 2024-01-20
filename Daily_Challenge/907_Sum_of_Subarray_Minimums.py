# 907 - Sum of Subarray Minimums
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        total_sum = 0

        left = [-1] * n 
        right = [n] * n
        def get_next_smaller_element_left():
            stack = []
            for i, value in enumerate(arr):
                while stack and arr[stack[-1]] >= value:  
                    stack.pop()  
                if stack:
                    left[i] = stack[-1]  
                stack.append(i) 
        def get_next_smaller_element_right():
            stack = []
            for i, value in enumerate(arr[::-1]):
                i = n - i - 1
                while stack and arr[stack[-1]] > value:  
                    stack.pop()  
                if stack:
                    right[i] = stack[-1]
                stack.append(i) 
        get_next_smaller_element_left()
        get_next_smaller_element_right()

        start = 0
        for position, value in enumerate(arr):
            p_left = left[position] 
            p_right = right[position] 
            
            length = p_right - p_left
            combinations = (p_right-position) * (position-p_left)
            mult_value = (combinations * value) % MOD
            
            #print(value, ':', length, combinations)
            
            total_sum = (total_sum + mult_value) % MOD
        
        return total_sum
