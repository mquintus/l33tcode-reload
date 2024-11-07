# 2275 - Largest Combination With Bitwise AND Greater Than Zero
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        all_set = 0
        curr_set = 0
        curr_bit = 1
        relevant_bits = []

        for bit in range(32):
            for c in candidates:
                if curr_bit & c > 0:
                   #print("Match", curr_bit, c,curr_bit & c)
                   curr_set += 1 
            #print(curr_bit, curr_set)
            all_set = max(all_set, curr_set)
            curr_set = 0
            curr_bit <<= 1

        return all_set

