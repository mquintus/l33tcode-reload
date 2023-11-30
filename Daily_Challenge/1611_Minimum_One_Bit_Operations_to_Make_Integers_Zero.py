# 1611 - Minimum One Bit Operations to Make Integers Zero
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        '''
            Intuition:
            Let's think of the lowest order bit as a gun, shooting 1s to the left.
            Operation is like (big brain strikes again...)

            1          the first bit can always be changed (0 steps for this capability)
            1     1    
            1    11    the second bit can only be changed when the first bit was changed
            1    1     (1 step)
            1   11     the third step requires to set and unset the first bit and to set 
            1   111    the second bit.
            1   1 1 
            1   1      In order to access the fourth bit, the third bit must be set only 
            1  11      which requires 7 operations to be set
            1  11 1
            1  1111    and to undo the third bit again takes 7 operations
            1  111 
            1  1 1 
            1  1 11
            1  1  1 
            1  1       Here the third bit is unset. The fourth bit is the rightmost bit.
            1 11   
            1 11  1    Reaching the fourth bit allowed us to set the fifth bit, but now
            1 11 11    the fourth bit must be un-set.
            1 11 1     That takes 2x 7 operations as well.
            1 1111 
            1 11111
            1 111 1
            1 111  
            1 1 1  
            1 1 1 1
            1 1 111
            1 1 11 
            1 1  1  
            1 1  11 
            1 1   1 
            1 1   
            111        Setting the fifth bit was successful, and took 32 steps
            111   1

            My working assumption is that the answer lies in powers of two.

            Change the 
            1 bit: 1 operation
            2 bit: 3 operations
            3 bit: 7 operations
            4 bit: 15 operations
            5 bit: 31 operations

            
            In order to be able to change bit n,
            we must change bit n-1 twice
            and then once change bit n.

            To reset a number n to 0, the way would be to...
            - identify the second left bit
            - if it can be changed, change it.
            - if it can't be changed, bring the second-highest bit
              one up.

            What to do in this scenario?
            1 1 1 1 1 
            Remove all bits right of the second-highest bit
            
            So the formula is 
            cost(8) - cost(6) + cost(4) - cost(2) + cost(0)

            or cost(highest_onebit) - cost(second_highest_onebit) + cost(third) - cost(fourth) ...

            The time complexity of this approach is O(b) with b the number of bits in the number.
            Or just O(1) if we assume that we always have 32 bits or 64 bits.

            Space complexity: Storing at most 64 numbers in an array.
            is O(64) or O(b)
        '''

        def cost_single_bit(index):
            return 2**(index+1)-1

        def cost_configuration(indexes):
            cost = 0
            for i, index in enumerate(sorted(indexes, reverse=True)):
                if i % 2 == 0:
                    cost += cost_single_bit(index)
                #elif i == 1:
                #    cost -= cost_single_bit(index)
                else:
                    cost -= cost_single_bit(index)
            return cost
        
        def solve(n):
            string_repr = "{0:b}".format(n)
            indexes = []
            for i, d in enumerate(string_repr[::-1]):
                if d == "1":
                    indexes.append(i)
            return cost_configuration(indexes)
        
        return solve(n)



    
