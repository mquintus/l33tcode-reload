# 1838 - Frequency of the Most Frequent Element
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr_k = k
        max_seq = 1
        seq = 1
        left_pointer = 0
        right_pointer = 0
        current_height = nums[left_pointer]
        while left_pointer < len(nums) - 1 and right_pointer < len(nums) - 1:
            # Can we move the right pointer to the right?
            diff_vertical = (nums[right_pointer + 1] - current_height) 
            diff_horizontal = (right_pointer + 1) - left_pointer
            diff_together = diff_vertical * diff_horizontal

            #print("left_pointer", left_pointer)
            #print("right_pointer", right_pointer)
            #print("diff_together <= curr_k???", diff_together, curr_k)

            if diff_together <= curr_k:
                seq += 1
                max_seq = max(max_seq, seq)
                curr_k -= diff_together 
                right_pointer += 1
                current_height = nums[right_pointer]
                continue
            else:
                seq -= 1
                free_vertical = current_height - nums[left_pointer]
                left_pointer += 1
                curr_k += free_vertical
                if left_pointer > right_pointer:
                    right_pointer += 1
                    current_height = nums[right_pointer]
                    seq = 1
                    

        return max_seq


        

