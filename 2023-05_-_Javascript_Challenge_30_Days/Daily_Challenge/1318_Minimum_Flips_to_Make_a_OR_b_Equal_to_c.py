class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        '''
        The minimum flips required in a or b 
        to let (a OR b == c) evaluate to true.

        Looking at each individual bit, we have 
        two options for c: 0 or 1
        - If c is 0, then both a and b must be 0 as well.
        This is either zero, one or two operations.

        - If c is 1, either a or b must be 1.
        This is either zero or one operation.
        The relevant bits can be found using XOR.

        Count the bits that need to be set to 1:
        - ((A OR B) ^ C) & C
        
        Count the bits that need to be set to 0:
        - (A == C) & !C
          + 
          (B == C) & !C


        First, we write a function that counts set bits
        Then, we do the operations as described
        '''
