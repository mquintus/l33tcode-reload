# 1358 - Number of Substrings Containing All Three Characters
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counts = [0,0,0]
        p0 = 0
        p1 = -1
        combinations = 0
        while p1 < len(s):
            p1 += 1
            if p1 == len(s):
                break
            counts[ord(s[p1])-ord('a')] += 1
            while counts[0]>0 and counts[1]>0 and counts[2]>0:
                new = len(s)-p1
                #print("New:", new, "after", s[p0:p1+1])
                combinations += new
                counts[ord(s[p0])-ord('a')] -= 1
                p0 += 1
        return combinations                   
                
