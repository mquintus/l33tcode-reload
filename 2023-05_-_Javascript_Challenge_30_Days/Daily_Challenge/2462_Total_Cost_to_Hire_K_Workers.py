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
        from the left list also removes them from the right list
        '''
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

        def refill(myList, sign='1'):
            not_found = 0
            new_el = None
            while new_el is None and len(costs_with_index) > candidates + not_found:
                new_el = costs_with_index[sign * (candidates + not_found - 1)]
                not_found += 1
            killindex = 0
            if new_el is not None:
                new_el = (new_el[0], new_el[1],)
                heapq.heappush(myList, new_el)
                killindex = new_el[1]
            return killindex

        while number_hired < k:
            number_hired += 1
            left_smallest = heapq.nsmallest(1, left)[0]
            right_smallest = heapq.nsmallest(1, right)[0]

            if left_smallest[0] <= right_smallest[0]:
                heapq.heappop(left)
                that_index = left_smallest[1]
                listindex = refill(left, 1)
                if left == []:
                    left = [i for i in right]
                if that_index == right_smallest[1]:
                    heapq.heappop(right)
                    listindex2 = refill(right, -1)
                    costs_with_index[listindex2] = None
                curr_cost = left_smallest[0]

                costs_with_index[listindex] = None
            else:
                heapq.heappop(right)
                curr_cost = right_smallest[0]


                #refill heap
                listindex2 = refill(right, -1)
                costs_with_index[listindex2] = None
            total_cost += curr_cost
        
        return total_cost

