class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Sometimes, when you've worked too much with a hammer, all problems start looking like a nail.
        I feel like using hashmaps a lot.
        Maybe, for this problem, a heap would be suited better.
        Let's discuss!

        When searching for the most frequent number, the naive approach is to keep a new counter
        for each distinct element.
        This way, we only need to iterate once the original list
        and then iterate the counter list to select the element that occured most often.
        '''
