# 214 - Shortest Palindrome
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        steps_counted = 0
        midpoint = (len(s)+1) / 2
        #
        # If is Palindrom: Return steps_counted
        # While not Palindrome: Add 1 to steps counted.
        #
        # Move the midpoint left by .5
        # Reduce length by .5
        
        def valid(p):
            if p == int(p):
                #print(p, s[0:int(p)], s[int(2*p)-1:int(p-1):-1])
                return s[0:int(p)] == s[2*int(p)-1:int(p-1):-1]
            #print(p, s[0:int(p)], s[int(2*p)-1:int(p):-1])
            return s[0:int(p)] == s[int(2*p)-1:int(p):-1]
        if valid(midpoint):
            return s

        while not valid(midpoint):
            #print(steps_counted, midpoint, s[int(midpoint+.5)], valid(midpoint))
            midpoint -= .5
            steps_counted += 1
        #print(steps_counted, midpoint, s[int(midpoint+.5)], valid(midpoint))

        if midpoint == int(midpoint):
            return s[int(midpoint):][::-1] + s[int(midpoint):]
        return s[int(midpoint+.5):][::-1] + s[int(midpoint)] + s[int(midpoint+.5):]
