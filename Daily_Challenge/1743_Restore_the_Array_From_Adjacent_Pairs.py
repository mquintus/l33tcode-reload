# 1743 - Restore the Array From Adjacent Pairs
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        '''
        Intuition:
        ----------
        This is a classical example of when to use hash maps.
        When parsing a pair (p1, p2), the hashmap will store two entries pointing to the other element
        p1: [p2]
        p2: [p1]
        When parsing another pair (p2, p3), the hashmap will update existing entries to result in:
        p1: [p2]
        p2: [p1, p3]
        p3: [p2]
        Each entry in the hashmap has two neighbors or, in case of the ends of the list, only one neighbor.
        
        We also must keep track of the ends of the list, i.e. a starting point. 
        
        For simplicity's sake, this can be done by iterating a second time over the resulting hashmap
        and return the first element that has only one neighbor.

        Complexity
        ----------
        For the time complexity evaluation, we assume p to be the number of pairs in the input
        and therefore n = p + 1, the number of elements in the list.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        
        myHashmap = {}
        # First loop
        for left, right in adjacentPairs:
            for element in [left, right]:
                if element not in myHashmap:
                    myHashmap[element] = []
            myHashmap[left].append(right)
            myHashmap[right].append(left)

        # Second loop
        for left, right in myHashmap.items():
            if len(right) == 1:
                break

        # Third loop
        result = []
        previous_node = float('inf')
        while left is not None:
            result.append(left)
            for neighbor in myHashmap[left]:
                if neighbor != previous_node:
                    previous_node = left
                    left = neighbor
                    break
            else:
                # If no right node was found, the next "left" is reset to None
                left = None
        
        return result
