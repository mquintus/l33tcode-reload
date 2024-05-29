# 1404 - Number of Steps to Reduce a Number in Binary Representation to One
class Solution:
    def numSteps(self, s: str) -> int:
        carry = 0
        steps = 0
        for bit in s[::-1]:
            steps += 1
            if bit == "1":
                doublecarry = 0
                if carry == 1:
                    doublecarry = 1
                    #steps += 1
                carry = 1
            elif bit == "0" and carry == 1:
                steps += 1
                carry = 1
                
        if doublecarry == 1:
            steps += 2
        return steps - 1
