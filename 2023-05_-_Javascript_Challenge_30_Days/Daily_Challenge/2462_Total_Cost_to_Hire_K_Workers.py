import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        '''
        This effectively is a k-smallest problem
        with two twists:
            - We can select from two subsets and must choose the better
            - Subsets and indexes might change after each selection
        
        The intuitive approach is to loop both the cost subsets 
        and put them into a minheap.

        The annoying thing is when they overlap, removing a worker 
        from the left list also removes them from the right list,
        so want I am going to do is, to override that worker with
        None in the original list and when pulling new workers,
        check if it is None and skip.
        '''

        total_cost = 0
        number_hired_left = 0
        number_hired_right = 0

        costs_with_index = []
        for i, v in enumerate(costs):
            costs_with_index.append((v, i,))

        left = costs_with_index[:candidates]
        heapq.heapify(left)

        right = costs_with_index[-candidates:]
        heapq.heapify(right)

        def refill_right(number_hired_right):
            if len(costs_with_index) > candidates + number_hired_right:
                not_left = 0
                new_right = None
                while new_right is None and len(costs_with_index) > candidates + number_hired_right + not_left:
                    new_right = costs_with_index[-1 * candidates - number_hired_right - 1 - not_left]
                    not_left += 1
                if new_right is not None :
                    heapq.heappush(right, new_right)      
                number_hired_right += 1

        while number_hired_left + number_hired_right < k:
            left_smallest = heapq.nsmallest(1, left)[0]
            right_smallest = heapq.nsmallest(1, right)[0]

            if left_smallest[0] <= right_smallest[0]:
                heapq.heappop(left)
                that_index = left_smallest[1]
                if that_index == right_smallest[1]:
                    heapq.heappop(right)
                    refill_right(number_hired_right)
                curr_cost = left_smallest[0]
                number_hired_left += 1

                costs_with_index[that_index] = None

                # refill heap
                if len(costs_with_index) > candidates + number_hired_left:
                    not_right = -1
                    new_left = None
                    while new_left is None and candidates + number_hired_left + not_right < len(costs_with_index):
                        new_left = costs_with_index[candidates + number_hired_left + not_right]
                        not_right += 1
                    if new_left is not None:
                        heapq.heappush(left, new_left)
            else:
                heapq.heappop(right)
                curr_cost = right_smallest[0]

                costs_with_index[right_smallest[1]] = None

                #refill heap
                refill_right(number_hired_right)
                number_hired_right += 1
            total_cost += curr_cost
        
        return total_cost

