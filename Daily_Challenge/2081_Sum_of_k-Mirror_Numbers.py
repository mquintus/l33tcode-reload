# 2081 - Sum of k-Mirror Numbers
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
            return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

        def isPalindrom(el, k):
            baseNresult = baseN(el, k)
            if baseNresult == baseNresult[::-1]:
                #print(baseNresult)
                return True
            return False
            
        def createPalindrome(num: int, odd: bool) -> int:
            x = num
            if odd:
                x //= 10
            while x > 0:
                num = num * 10 + x % 10
                x //= 10
            return num

        solution = 0
        length = 1
        while n > 0:
            for odd in [True, False]:
                for i in range(length, length * 10):
                    if n <= 0:
                        break
                    pal = createPalindrome(i, odd)
                    if isPalindrom(pal, k): 
                        solution += pal
                        #print(n, pal)
                        n -= 1
            length *= 10
        return solution
