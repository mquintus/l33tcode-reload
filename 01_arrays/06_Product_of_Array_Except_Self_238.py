class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Naive solution: Use a double loop
        has a time complexity of O(n^2) and is therefore not a viable solution.

        Next naive idea: 
        Iterate once and calculate the total product.
        Then iterate once more, for each element and divide the total product by the element and write down
        Problem: Division operation is prohibited.
        Problem: Also if a value is 0 then the total product is zero 

        More ideas: 
        - Use some sort of masking while applying the multiply operation on the whole list?
        - This problem has many reoccuring calculations. Caching might help here.
          - Generate a binary tree of multiplied and cached values
          - but constructing such a tree also requires O(n log n) 

        An algorithm that runs in O(n) time would visit every number only once.
        We already know that the result list has a fixed length of n * 32 bit.


        So let's 
        a) Initialize the result list with 1 values and start multiplying immediately:    O(n)
        b) If we come from both sides we might get a linear solution: 2*O(n)
        c) In the final run, we can multiply the left and the right value of each cell: 3*O(n)
        '''

        total_product_left = [1]
        for i in range(len(nums) - 1):
            total_product_left.append(total_product_left[-1] * nums[i])

        total_product_right = [1]
        for i in range(len(nums) - 1, 0, -1):
            total_product_right.insert(0, total_product_right[0] * nums[i])

        ret = []
        for i in range(len(nums)):
            ret.append(total_product_left[i] * total_product_right[i])

        return ret
