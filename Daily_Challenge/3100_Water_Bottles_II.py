# 3100 - Water Bottles II
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        # after each action, numExchange is increased by one
        # therefore the number of bottles that I initially can swap in is
        # numExchange or 2*numExchange+1 or 3*numExchange+2 or ...
        # I could implement binarySearch but the maxvalue is 100, so lets go for the simulation approach

        drunk = 0 
        while numBottles >= numExchange:
            drunk += numExchange
            numBottles -= numExchange
            numExchange += 1
            numBottles += 1
        drunk += numBottles
        return drunk
