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
        '''
