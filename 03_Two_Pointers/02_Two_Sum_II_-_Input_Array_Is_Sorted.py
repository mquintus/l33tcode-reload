class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        The two sum question can be solved using a hash map 
        where you iterate over the the array once, store all numbers in a hashmap
        and then just check for each number if the complement is already there.
        This works well, even on unsorted input arrays, but requires O(N) space.

        Since we have a sorted array, we can use this property.
        We use two pointers, one from the beginning and one from the end.
        We add the two numbers and compare it with the target.
        If the target is smaller, we decrease the second pointer.
        If the target is bigger, we increase the first pointer.
        Sounds fun. Let's go.
        '''

        '''
        Any edge cases?
        Maybe we need to put in additional thought about negative numbers.
        Actually: no. The solution is fine, as long as we have guaranteed only 1 solution and at least two elements in the array.
        '''
        p0 = 0
        p1 = len(numbers) - 1

        mySum = numbers[p0] +numbers[p1]
        while mySum != target and p0 < p1:
            if mySum < target:
                p0 += 1
            if mySum > target:
                p1 -= 1
            mySum = numbers[p0] + numbers[p1]

        return [p0+1, p1+1]
'''
[2,7,11,15]
9
[2,3,4]
6
[-1,0]
-1
[-1,0,1,2,3,4,5,6,7,8,9,100,500,999,1000]
998
[-1,0,1,2,3,4,5,6,7,9,100,500,999,1000]
99
[0,1,2,3,4,7,9,100,500,999,1000]
8
[0,1,2,3,4,5,6,7,9,100,500,999,1000]
101
'''
