import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        '''
        This effectively is a k-smallest problem
        with two twists:
            - We can select from two subsets and must choose the better
            - Subsets and indexes might change after each selection
            - When pulling a number from the left of the subsets, it might
              disappear in the right as well
        
        The intuitive approach is to loop both the cost subsets 
        and put them into a minheap.

        The annoying thing is when they overlap, removing a worker 
        from the left list also removes them from the right list
        '''
        if candidates * 2 >= len(costs) or k >= len(costs):
            return sum(sorted(costs)[:k])

        number_hired = 0
        total_cost = 0
        costs_with_index = []
        for i, v in enumerate(costs):
            costs_with_index.append((v, i,))

        left = costs_with_index[:candidates]
        heapq.heapify(left)

        right = costs_with_index[-candidates:]
        heapq.heapify(right)

        for i in range(len(left)):
            costs_with_index[i] = None
        for i in range(len(right)):
            idx = len(costs_with_index) - 1 - i
            costs_with_index[idx] = None

        def next_worker(sign='1', skip=0):
            if sign == -1:
                skip += 1
            idx = sign * (candidates + skip)
            if sign == -1:
                idx = len(costs_with_index) + idx
            new_el = None
            if idx < len( costs_with_index) and idx >= 0:
                new_el = costs_with_index[idx]
            return new_el
        
        hired_left = 0
        hired_right = 0
        overlap = False
        for number_hired in range(k):
            next_left = next_worker(1, hired_left)
            next_right = next_worker(-1, hired_right)
            
            if len(right) == 0 or left[0][0] <= right[0][0]:
                left_smallest = left[0]
                hired_left += 1

                if next_left is not None:
                    heapq.heapreplace(left, next_left)
                else:
                    heapq.heappop(left)

                that_index = left_smallest[1]
                
                ## If the item is also in the right list,
                ## Remove it there also.
                ## No need to refill on the right: We know there is an overlap,
                ## therefore we can always find any item in the left list.
                if len(right) > 0:
                    right_smallest = right[0]
                    if that_index == right_smallest[1]:
                        popped_right = heapq.heappop(right)
                        assert popped_right[1] == that_index
                        overlap = True
                    
                curr_cost = left_smallest[0]
                costs_with_index[left_smallest[1]] = None
            else:
                right_smallest = right[0]
                hired_right += 1
                if not overlap and next_right is not None:
                    heapq.heapreplace(right, next_right)
                else:
                    heapq.heappop(right)
                curr_cost = right_smallest[0]
                costs_with_index[right_smallest[1]] = None
            total_cost += curr_cost
        
        return total_cost

