# 632 - Smallest Range Covering Elements from K Lists
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        heap = []
        preheap = []
        pointers = [0] * len(nums)
        for i, group in enumerate(nums):
            heapq.heappush(preheap, (group[0], i))
            
        while preheap:
            val, i = heapq.heappop(preheap)
            pointers[i] += 1
            if pointers[i] < len(nums[i]):
                while pointers[i] < len(nums[i]) and nums[i][pointers[i]] == val:
                    pointers[i] += 1
                if pointers[i] < len(nums[i]):
                    heapq.heappush(preheap, (nums[i][pointers[i]], i))
            heap.append((val, i))
        
        p_small = 0
        p_large = -1
        including = 0
        included = [0] * k

        best_range_l = float('inf')
        best_range = []

        while p_large < len(heap):
            while including < k:
                p_large += 1
                if p_large == len(heap):
                    return best_range
                group_id = heap[p_large][1]
                if included[group_id] == 0:
                    including += 1
                included[group_id] += 1

            while including == k:
                curr_range = [heap[p_small][0], heap[p_large][0]]
                curr_range_l = heap[p_large][0]-heap[p_small][0]
                #print(small, big, "Distance", curr_range_l)
                if curr_range_l < best_range_l:
                    best_range_l = curr_range_l
                    best_range = curr_range
                if best_range_l == 0:
                    return best_range
                    
                group_id = heap[p_small][1]
                included[group_id] -= 1
                if included[group_id] == 0:
                    including -= 1
                p_small += 1
