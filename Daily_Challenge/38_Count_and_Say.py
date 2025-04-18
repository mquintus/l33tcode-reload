# 38 - Count and Say
class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(s):
            enc = ""
            prev = s[0]
            c = 1
            for el in s[1:]:
                if el != prev :
                    enc += str(c) + prev
                    c = 0
                c += 1
                prev = el
            enc += str(c) + prev
            return enc
                    
        enc = "1"
        for i in range(1,n):
            enc = rle(enc)
        return enc
