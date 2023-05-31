class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Sometimes, when you've worked too much with a hammer, all problems start looking like a nail.
        I feel like using hashmaps a lot.
        Maybe, for this problem, a heap would be suited better.
        Let's discuss!

        When searching for the most frequent number, the naive approach is to keep a new counter
        for each distinct element.
        This way, we only need to iterate once the original list (O(n))
        and then iterate the counter list to select the element that occured most often.

        However, looping over the counter list will take another O(n) of time complexity,
        resulting in O(n^2)
        and we want to stay below that.

        If we use a heap to structure the counters, then
        the list can stay sorted while we are updating it.

        A max head keeps the largest element at the top.

        At the end, we need to pop from the heap with O(log k)
        but actually k times to get the k elements with O(k log k) as the worst case.
        Since we are considering the average case,
        can be reduced to O(log k).

        So the final time complexity is O(n log k).

        Another challenge here is to access the Counters in constant time while storing them in the heap.
        So we need a book-keeping structure 
        for each found number 
        - with a pointer to the heap element (to update)
        - with a counter 

        This sounds a lot like a priority queue.
        '''
        def heap_solution(nums: List[int], k: int) -> List[int]:
            from heapq import heappop, heappush, heapify

            my_max_heap = []
            my_counter = {}
            tasks = {}

            if len(nums) == 1:
                '''Only one elemt: Is already sorted'''
                return nums

            for mynum in nums:
                ''' Get the next number '''
                if mynum not in my_counter.keys():
                    ''' 
                    If it is a fresh number, 
                    a) set the counter to -1
                    Since we are using a minheap, we want the counter to be negative to always
                    have the most occurences at the top. 
                    b) Create a new "task" for the priority queue
                    c) Add the task to the hashmap (to find it immediately if we need to change it)
                    d) Add the task to the priority queue / minheap
                    '''
                    my_counter[mynum] = -1
                    task = [my_counter[mynum], mynum]
                    tasks[mynum] = task
                    heappush(my_max_heap, task)
                else:
                    '''
                    If the number is already known:
                    a) Increase the hashmap counter
                    b) Update the task within the heap, damaging the constraints
                    c) Re-Heapify
                       This action can be implemented more efficiently if we already
                       know which element changed, but since we don't want to dive into
                       this problem with our own heap implementation, we leave this as an
                       exercise to the reader.
                    '''
                    my_counter[mynum] += -1
                    tasks[mynum][0] = my_counter[mynum]
                    heapq.heapify(my_max_heap)
            ''' 
            Finally let's pop the k "smallest" aka. largest tasks from the heap
            and return the number of that task.
            '''
            return [x[1] for x in heapq.nsmallest(k, my_max_heap)]
        # return heap_solution(nums, k)


        '''
        Let's revisit this challenge.
        There is a probabilistic approach for unsorted lists: Lomuto's Partition Scheme.
        It works with two pointers.
        The basic idea is that we select a "pivot" element from the end of the list and move up
        as long as the pivot is smaller and move other bigger elements to the left.

        This is an approach to replace the heap. The hashmap is still required.
        '''
        def lomuto_solution(nums: List[int], k: int) -> List[int]:
            # First half: time complexity O(n)
            counter = {}
            for i in nums:
                if i in counter.keys():
                    counter[i][0] += 1
                else:
                    counter[i] = [1, i]

            # Second half
            def swap(a,b):
                temp = counter[a]
                counter[a] = counter[b]
                counter[b] = temp

            # Through away the counter's index, turn it into a list
            counter = list(counter.values())

            # Pivot is at the end of the list
            pivot_position = len(counter) - 1
            # Store index is at 0
            store_index = 0
            target_position = len(counter) - k
            security_counter = len(counter)
            while store_index != target_position and security_counter > 0:
                store_index = 0
                security_counter -= 1
                pivot = counter[pivot_position]
                for j in range(store_index, pivot_position):
                    other = counter[j]
                    if other[0] <= pivot[0]:
                        swap(j, store_index)
                        store_index += 1
                swap(pivot_position, store_index)
                if store_index < target_position:
                    store_index += 1
                if store_index > target_position:
                    pivot_position = store_index - 1
                    store_index = 0
                #print("next pivot")
            
            return [el[1] for el in counter[-k:]]
        return lomuto_solution(nums, k)
