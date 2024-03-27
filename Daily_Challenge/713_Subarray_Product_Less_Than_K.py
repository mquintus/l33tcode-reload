# 713 - Subarray Product Less Than K
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p1 = 0
        p2 = 0
        product = nums[0]

        previously_matched = 0

        result_count = 0
        def add_all_subarrays(p1, p2, previously_matched,  result_count):
            #print("Adding options:", p1, p2, previously_matched)
            for start in range(p1, p2+1):
                result_count += (p2+1) - (max(start, previously_matched))
            return result_count

        while p2 < n:
            #print(product, p1, p2)
            if product >= k:
                if p2 > p1:
                    product /= nums[p1]
                    p1 += 1
                else:
                    p1 = p2 = p1 + 1
                    if p1 < n:
                        product = nums[p1]
                continue

            if p2 + 1 < n:
                if product * nums[p2 + 1] < k:
                    p2 += 1
                    product *= nums[p2]
                else:
                    previously_matched = max(p1, previously_matched)
                    result_count = add_all_subarrays(p1, p2, previously_matched, result_count)
                    previously_matched = max(p2, previously_matched) + 1
                    p2 += 1
                    product *= nums[p2]
                    product /= nums[p1]
                    p1 += 1
            else:
                #add_all_subarrays(p1, p2)
                break
        if product < k:
            previously_matched = max(p1, previously_matched)
            result_count = add_all_subarrays(p1, p2, previously_matched, result_count)
            previously_matched = max(p2, previously_matched) + 1
        #print(result_count)
        return result_count
