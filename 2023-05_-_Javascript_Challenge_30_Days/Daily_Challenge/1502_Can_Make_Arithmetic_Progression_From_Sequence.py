class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        '''
        I am working on this challenge as part of the "daily challange" streak.
        Yesterday's challenge was similar in that one was supposed to identfy if points were on a line.

        Today's challenge is even more straight forward, in the sense that the steps towards
        the solution are already laid out: sort, and then check if the distance between each element
        is the same.

        Time complexity: O(n log n)
        Space complexity: O(n)
        '''
        def naive_solution(arr: List[int]) -> bool:
            arr = sorted(arr)
            #print("Sorted:", arr)
            dist = arr[1] - arr[0]
            prev = arr[1]
            for el in arr[2:]:
                #print(el, prev, dist)
                if el - prev != dist:
                    #print("FALSE:", el, prev, dist)
                    return False
            return True
        # return naive_solution(arr)

        ''' 
        Let's check if we can do it faster.
        If we looped through all elements, we can store them in a hashtable,
        and we can find the distances between neighboring elements.
        If we store the smallest and the second smallest element, we can even derive the distance.
        So we need to check 
        - between the smallest and the largest element there are no holes.
        To check that, we can use the hashmap to validate.
        Time complexity: O(n)
        Space complexity: O(n)

        Also we need to check:
        - all elements in the hashtable are in the right distance
        Time complexity: O(n)
        Space complexity: O(1)
        
        The hashmap comes with logical complexity and opens new edge cases that were't important before.
        Edge cases: 
        - Duplicates (we have to check explicitly)
        - Distance zero: If all elements are the same, it's also a valid testcase
        - All items of the assumed iteration step exist, but additional items exist

        This solution is better in theoretical Big-O notation,
        but the overhead needs to be justified within production context.
        '''
        def hashtable_solution(arr: List[int]) -> bool:
            '''Edge case: Only two elements is always True'''
            if len(arr) < 3:
                return True

            hashtable = {}
            smallest_element = arr[0]
            second_smallest = arr[1]
            if smallest_element > second_smallest:
                smallest_element = arr[1]
                second_smallest = arr[0]
            largest_el = arr[2]

            # First loop: 
            # - Time complexity: O(n)
            # - Space complexity: O(n)
            for el in arr:
                if el in hashtable:
                    hashtable[el] += 1
                else:
                    hashtable[el] = 1
                if el < smallest_element:
                    second_smallest = smallest_element
                    smallest_element = el
                if el > smallest_element and el < second_smallest:
                    second_smallest = el

                if el > largest_el:
                    largest_el = el
            
            distance = second_smallest - smallest_element
            print(smallest_element, second_smallest, largest_el, distance)

            if distance == 0:
                if smallest_element == largest_el:
                    return True
                return False

            # Second loop:
            # - Time complexity: O(n)
            # - Space complexity: O(1)       
            for target in range(smallest_element, largest_el + 1, distance):
                if target not in hashtable:
                    return False
                if hashtable[target] > 1:
                    return False
                hashtable.pop(target)
                
            # Third loop:
            # - Time complexity: O(n)
            for el in arr:
                if el in hashtable:
                    return False

            #print(hashtable)
            return True

        #assert naive_solution(arr) == hashtable_solution(arr)
        if naive_solution(arr) != hashtable_solution(arr):
            print("Naive", naive_solution(arr))
            print("Hashtable", hashtable_solution(arr))
        return hashtable_solution(arr) 

