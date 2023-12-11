# 1287 - Element Appearing More Than 25% In Sorted Array
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        '''
        Intuition:
        If an element appears more than 25% of the time
        and it's a sorted array, where identical elements stick together then;
        let's cut the array into four pieces (if possible) and the element must overlap two of the quarters.
        
        Caveat: Since there are three cuts, there might be two other element that also overlap.
        We can use binary search to find the first and last of these identical elements and determine
        which one has the highest occurrence.
        '''
        n = len(arr)

        if n <= 3:
            # Edge case: If less than 4 elements,
            # there can only be one type of element.
            return arr[0]

        candidates = {}
        cuts = []
        cut_count = 5
        if n <= cut_count:
            cuts = range(1,n)
        else:
            cuts = list(set([int(n/cut_count * i) for i in range(1,cut_count)]))

        max_candidate = 0
        for cut in cuts:
            left = arr[cut - 1]
            right = arr[cut]

            if left == right:
                if left not in candidates:
                    candidates[left] = 0
                candidates[left] += 1
                max_candidate = max(candidates[left], max_candidate)


        #print(max_candidate)
        #for c, count in candidates.items():
        #    print(c, count)

        if len(candidates) == 1:
            return list(candidates.keys())[0]

        def binary_search_left_end(el):
            start = 0
            end = len(arr) - 1
            #print('-------------------')
            while start <= end:
                mid = (start + end) // 2
                if arr[mid] > el:
                    end = mid - 1
                elif arr[mid] < el:
                    start = mid + 1
                elif mid > 0 and arr[mid] == el and arr[mid - 1] == el:
                    end = mid - 1
                elif arr[mid] == el:
                    #print("We found", el, "and the leftmost occurence is at", mid)
                    break
            else:
                # print(el, "is nowhere to be found. It should be at", mid, "out of",n, " but there is", arr[mid])
                if arr[mid] < el:
                    mid += 1
            
            return mid

        #from collections import Counter
        #mycounter = Counter(arr)
        #print(mycounter)

        next_level_candidates = {}
        max_size = 0
        winner = -1
        for c in candidates:
            left = binary_search_left_end(c)
            right = binary_search_left_end(c + .5)
            size = right - left
            #print("Candidate:", c, "  Size:", size, "   Target:", n//4)
            if size >= n /4:
                next_level_candidates[c] = size
                max_size = max(max_size, size)
                if size == max_size:
                    winner = c

        return winner
