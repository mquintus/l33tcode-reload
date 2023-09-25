# 389 - Find the Difference
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        '''
        Beautiful constant size, linear time complexity solution.
        '''
        letters = 0
        i = -1
        for i in range(len(s)):
            letters -= ord(s[i])
            letters += ord(t[i])
        letters += ord(t[i + 1])
        
        return chr(letters)
        

