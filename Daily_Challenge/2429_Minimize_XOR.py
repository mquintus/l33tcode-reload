# 2429 - Minimize XOR
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bitcount = 0
        bitcount1 = 0
        bits = []
        # If the bitcount is less or equal, just go ahead and unset all bits starting from the biggest
        # If the bitcount is bigger, fill up the unset bits to get something like 11111111

        #print("bit_count",num2.bit_count())
        while num2 > 0:
            #print(num2, bitcount,num2 & 1)
            bitcount += (num2 & 1)
            num2 //= 2

        #print(bitcount)

        #print("bit_count",num1.bit_count())
        while num1 > 0:
            bitcount1 += (num1&1)
            bits.append(num1&1)
            num1 //= 2

        #print(bits[::-1], bitcount1)

        newbits = []
        #print(newbits, bitcount)
        for bitposition in range(len(bits) - 1, -1, -1):
            if bitcount > 0:
                if bits[bitposition] == 1:
                    bitcount -= 1
                newbits.append(bits[bitposition])
            else:
                newbits.append(0)

        #print(newbits, bitcount)
        
        for bitposition in range(len(bits) - 1, -1, -1):
            if bitcount > 0 and newbits[bitposition] == 0:
                newbits[bitposition] = 1
                bitcount -= 1
        
        #print(newbits, bitcount)
        
        while bitcount > 0:
            bitcount -= 1
            newbits.insert(0, 1)

        #print(newbits, bitcount)

        newnumber = 0
        curr = 1
        for bitposition in range(len(newbits) - 1, -1, -1):
            newnumber += newbits[bitposition] * curr
            curr *= 2

        return newnumber
