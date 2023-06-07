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
        '''
        def countSetBits(number):
            counter = 0
            #print(number)
            while number > 0:
                if number & 1: 
                    counter += 1
                number >>= 1
            return counter


        #assert countSetBits(7) == 3
        #assert countSetBits(6) == 2
        #assert countSetBits(5) == 2
        #assert countSetBits(4) == 1
        #assert countSetBits(3) == 2
        #assert countSetBits(2) == 1
        #assert countSetBits(1) == 1
        #assert countSetBits(0) == 0
        
        '''
        Then, we do the operations as described:
        '''
        bits_ctr = 0
        #print("bits_ctr", bits_ctr, "from",a ,b, "to", c)

        bits_needed_to_be_set_to_1 = ((a | b) ^ c) & c
        bits_ctr += countSetBits(bits_needed_to_be_set_to_1)
        #print("bits_needed_to_be_set_to_1", countSetBits(bits_needed_to_be_set_to_1), bits_ctr)

        bits_from_A_needed_to_be_set_to_0 = (a & ~c)
        bits_ctr += countSetBits(bits_from_A_needed_to_be_set_to_0)
        #print("bits_from_A_needed_to_be_set_to_0", countSetBits(bits_from_A_needed_to_be_set_to_0), bits_ctr)

        bits_from_B_needed_to_be_set_to_0 = (b & ~c)
        bits_ctr += countSetBits(bits_from_B_needed_to_be_set_to_0)
        #print("bits_from_B_needed_to_be_set_to_0", countSetBits(bits_from_B_needed_to_be_set_to_0), bits_ctr)

        return bits_ctr

