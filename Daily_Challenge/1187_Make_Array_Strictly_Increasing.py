class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        '''
        The challenge is to make arr1 strictly increasing.
        The possible actions are to replace numbers from arr1 with other numbers, found in arr2.
        We are looking for the minimum number of steps.

        For the first approximation, we can assume that arr1 is partly ordered 
        but we should also consider edge cases where arr1 needs to be completely replaced with
        elements from arr2

        Let's try some recursion.
        If the rest of the list can be sorted, we don't need to change the current number

        '''
        
        '''
        Ok, testcase 19/21 is making trouble.  Execeeded time limit.
        '''

        num_subst = 0
        arr2 = sorted(arr2)

        def helper(arr1, arr2, prev_num):
            changes = -1
            if len(arr1) == 0:
                return 0


            
            if prev_num >= arr1[0]:
                #
                # If the current number is lower than or equal to the previous number,
                # **not** changing the current number (myself) will not provide
                # a valid sorting.
                #
                keep_myself_changes_rest = -1
            else:
                # If the current number is in the right order, 
                # try to find a recursive solution for the rest of the numbers
                #
                keep_myself_changes_rest = helper(arr1[1:], arr2, arr1[0])

            change_myself_changes_rest = -1
            if keep_myself_changes_rest > 1 or keep_myself_changes_rest == -1:
                #
                # Even if the current number is in the right order, it might still be the 
                # best solution to substitute it with an even lower number from arr2.
                #
                # Therefore: calculate the changed version in the case where
                # I haven't found a solution
                # OR 
                # I have found a solution but it is greater than 1
                #
                for b in arr2:
                    # Loop the numbers b in arr2 (sorted) until 
                    # b is greater than prev_num
                    if b > prev_num:
                        # print("Substitute ", arr1[0], 'with', b)
                        arr1[0] = b
                        change_myself_changes_rest = helper(arr1[1:], arr2, b)
                        break

            # print(prev_num, arr1[0], keep_myself_changes_rest, change_myself_changes_rest)

            if change_myself_changes_rest == -1:
                return keep_myself_changes_rest 

            if keep_myself_changes_rest == -1:
                return change_myself_changes_rest + 1

            return min(keep_myself_changes_rest, change_myself_changes_rest + 1)


        return helper(arr1, arr2, -1) 

# Test cases:
'''
[1,5,3,6,7]
[1,3,2,4]
[1,5,3,6,7]
[4,3,1]
[1,2]
[100]
[7,6,5,4]
[1,3,2,4]
[17,16,15,3]
[5,3,2,4]
[11,12,13,10]
[1,3,2,4]
[1,5,4,3]
[11,12,13,10]
[1,14,15,13]
[10,11]
'''
