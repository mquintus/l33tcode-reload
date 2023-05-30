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
        but actually k times to get the k elements. Since k is a constant,
        O(k * log n) can be reduced to O(log n).

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

            while len(nums) > 0:
                mynum = nums.pop()
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


        return heap_solution(nums, k)
